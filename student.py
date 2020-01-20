import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add_recipes')
def add_recipes():
    return render_template("add_recipe.html")


if __name__ == "__main__":
        app.run(host=os.environ.get("IP"),
        port=os.environ.get("PORT"),
        debug=True)