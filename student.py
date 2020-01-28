import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'StudentLife'
app.config["MONGO_URI"] = 'mongodb+srv://LWin_01:01Libby@StudentLife-ldsrb.mongodb.net/StudentLife?retryWrites=true&w=majority'
                                    
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html", recipes=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html", page_title="Add Recipe",
    recipes=mongo.db.recipes.find())

    


if __name__ == "__main__":
        app.run(host=os.environ.get("IP"),
        port=os.environ.get("PORT"),
        debug=True)