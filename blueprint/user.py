from flask import Blueprint, render_template , request , redirect , url_for , flash
from flask_login import login_user , current_user , login_required
from passlib.hash import sha256_crypt
from models.user import User
from extention import db
from models.cart import Cart 
from models.cart_item import CartItem
from models.product import product as Product
from models.payment import Payment
import requests

app = Blueprint("user", __name__)

@app.route("/user/login" , methods = ["GET" , "POST"])
def login():
    if request.method == "GET":
        return render_template("user/login.html")
    else:
        register = request.form.get("register" , None)
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        phone = request.form.get("phone", None)
        address = request.form.get("address", None)

        if register != None:
            user = User.query.filter(User.username == username).first()
            if user != None:
                flash("این نام کاربری قبلا استفاده شده است")
                return redirect(url_for("user.login"))


            user = User(username = username , password= sha256_crypt.encrypt(password) , phone = phone , address = address)
            db.session.add(user)
            db.session.commit()
            login_user(user)

            return redirect(url_for("user.dashboard"))

        else:
            user = User.query.filter(User.username == username).first()
            if user == None:
                flash("نام کاربری یا رمز اشتباه است")
                return redirect(url_for("user.login"))

            if sha256_crypt.verify(password, user.password):
                login_user(user)
                return redirect(url_for("user.dashboard"))
            else:
                flash("نام کاربری یا رمز اشتباه است")
                return redirect(url_for("user.login"))


    
        return "ok"




@app.route("/add-to-cart", methods=["GET"])
@login_required
def add_to_cart():
    id = request.args.get("id")

    product = Product.query.filter(Product.id == id).first_or_404()

    cart = Cart.query.filter(
        Cart.user_id == current_user.id,
        Cart.status == "pending"
    ).first()

    if cart is None:
        cart = Cart(user_id=current_user.id)
        db.session.add(cart)
        db.session.commit()

    cart_item = CartItem.query.filter(
        CartItem.cart_id == cart.id,
        CartItem.product_id == product.id
    ).first()

    if cart_item is None:
        cart_item = CartItem(
            quantity=1,
            price=product.price,
            cart_id=cart.id,
            product_id=product.id
        )
        db.session.add(cart_item)
    else:
        cart_item.quantity += 1

    db.session.commit()

    return redirect(url_for("user.cart"))

@app.route("/remove-from-cart", methods=["GET"])
@login_required
def remove_from_cart():
    id = request.args.get("id")
    cart_item = CartItem.query.filter(CartItem.id == id).first_or_404()
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
    else:
        db.session.delete(cart_item)

    db.session.commit()
    return redirect(url_for("user.cart"))



@app.route("/cart" , methods = ["GET"])
@login_required
def cart():
    cart = current_user.carts.filter(Cart.status == "pending").first()
    return render_template("user/cart.html", cart=cart)

@app.route("/payment" , methods = ["GET"])
@login_required
def payment():
    cart = current_user.carts.filter(Cart.status == "pending").first()

    r = requests.post("https://sandbox.shepa.com/api/v1/token",
                       data={
                            "api" : "sandbox",
                            "amount" : cart.total_price(),
                            "callback": "http://localhost:5000/verify"
                        })

    tokan = r.json()["result"]["token"]
    url = r.json()["result"]["url"]

    
    pay = Payment( price=cart.total_price(),token=tokan)
    pay.cart = cart
    db.session.add(pay)
    db.session.commit()

    return redirect(url)


@app.route("/verify" , methods = ["GET"])
@login_required
def verify():
    token = request.args.get("token")
    pay = Payment.query.filter(Payment.token == token).first_or_404()


    r = requests.post("https://sandbox.shepa.com/api/v1/verify",
                       data={
                            "api" : "sandbox",
                            "amount" : pay.price,
                            "token": token
                        })

    pay_status = r.json()["success"]
    if pay_status == "true" :
        transaction_id = r.json()["result"]["transaction_id"]
        refid = r.json()["result"]["refid"]
        card_pan = r.json()["result"]["card_pan"]


        pay.card_pan = card_pan
        pay.transaction_id = transaction_id
        pay.refid = refid
        pay.status = "success"
        pay.cart.status = "paid"
    else:
        pay_status = "failed"

    db.session.commit()
    

    return redirect(url_for("user.dashboard"))

@app.route("/user/dashboard" , methods = ["GET"])
@login_required
def dashboard():
    return "Here is the dashboard"