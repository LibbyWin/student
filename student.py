import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
#to get secret key file
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)
app.secret_key = os.getenv("Secret")
#get secret key
app.config["MONGO_DBNAME"] = 'StudentLife'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")   
                                    
mongo = PyMongo(app)

#Connects the home page to mongodb in order to show the recipes 
@app.route('/')
def index():
    recipes=mongo.db.recipes.find()
    categories=mongo.db.categories.find()
    return render_template("index.html", recipes=recipes, categories=categories,)

#allowing you to add a whole new recipe to the database and site
@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html", page_title="Add Recipe", 
    recipes=mongo.db.recipes.find(),
    categories=mongo.db.categories.find())

#allowing you to add a whole new recipe to the database and site
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes=mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('/'))

#Previewing the whole recipe information
@app.route('/view_recipe/<recipes_id>')
def view_recipe(recipes_id):
   the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
   all_category = mongo.db.category.find() 
   return render_template("view_recipe.html", recipes=the_recipe, category=all_category)

#editing recipe information
@app.route('/edit_recipe/<recipes_id>')
def edit_recipe(recipes_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    all_category = mongo.db.category.find()
    return render_template("edit_recipe.html", recipes=the_recipe, category=all_category)

#Updating your recipes
@app.route('/update_recipe/<recipes_id>', methods=["POST"])
def update_recipe(recipes_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipes_id)},
    {
        #Allows for each new recipe to be given these names and to locate/contain the provided info within the names
            "name": request.form.get["name"],
            "category_name": request.form.get["category"],
            "serves": request.form.get["serves"],
            "price": request.form.get["price"],
            "protein": request.form.get["protien"],
            #.split("/n") allows for all new inputs to be added on a new line
            "ingredients": list(request.form.get["ingredients"].split("\n")),
            #.split("/n") allows for all new inputs to be added on a new line
            "instructions": list(request.form.get["instructions"].split("\n")),
            "description": request.form.get["description"],
            "image": request.form.get["image_url"],
    })
    return redirect(url_for('index'))

#For deleting recipes
@app.route('/delete_recipe/<recipes_id>')
def delete_recipe(recipes_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipes_id)})
    return redirect(url_for('/'))


if __name__ == "__main__":  
        app.run(host=os.environ.get("IP"),
        port=os.environ.get("PORT"),
        debug=True)