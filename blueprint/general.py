from flask import Blueprint, render_template, request
from models.product import product
from models.product import product as Product


app = Blueprint("general", __name__)

@app.route("/")
def main():
    search = request.args.get("search", None)

    products = Product.query.filter(Product.active == 1)

    if search != None:
        products = products.filter(Product.name.like(f"%{search}%"))
        
    product = products.all()


    return render_template("main.html", products=products, search = search)

@app.route("/product/<id>/<name>")
def product_page(id, name):
    product = Product.query.filter(Product.id == id).filter(Product.name == name).filter(Product.active == 1).first_or_404()
    return render_template("product.html", product=product)
@app.route("/about")
def about():
    return render_template("about.html")