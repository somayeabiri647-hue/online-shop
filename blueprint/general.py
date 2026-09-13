from flask import Blueprint, render_template
from models.product import product
from models.product import product as Product


app = Blueprint("general", __name__)

@app.route("/")
def main():
    products = product.query.filter(product.active == 1).all()
    return render_template("main.html", products=products)

@app.route("/product/<id>/<name>")
def product_page(id, name):
    product = Product.query.filter(Product.id == id).filter(Product.name == name).filter(Product.active == 1).first_or_404()
    return render_template("product.html", product=product)
@app.route("/about")
def about():
    return render_template("about.html")