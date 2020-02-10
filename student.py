import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# to get secret key file
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.getenv("Secret")
# get secret key
app.config["MONGO_DBNAME"] = 'StudentLife'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

# Connects the home page to mongodb in order to show the recipes
@app.route('/')
@app.route('/index')
def index():
    recipes = mongo.db.recipes.find()
    categories = mongo.db.categories.find()
    return render_template(
        "index.html",
        recipes=recipes,
        categories=categories,)

# allowing you to add a whole new recipe to the database and site
@app.route('/add_recipe')
def add_recipe():
    recipe = mongo.db.recipes.find()
    categories = mongo.db.categories.find()
    return render_template(
        "add_recipe.html",
        recipes=recipe,
        categories=categories)

# allowing you to add a whole new recipe to the database and site
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    print(request.form)
    ingredients = request.form.get('ingredients').splitlines()
    instructions = request.form.get('instructions').splitlines()
    recipe_insert = {
        'name': request.form.get('name'),
        'category_name': request.form.get('category_name'),
        'serves': request.form.get('serves'),
        'price': request.form.get('price'),
        'protein': request.form.get('protein'),
        'ingredients': ingredients,
        'instructions': instructions,
        'description': request.form.get('description'),
    }
    recipes.insert_one(recipe_insert)

    return redirect(url_for('index'))

# Previewing the whole recipe information
@app.route('/view_recipe/<recipes_id>')
def view_recipe(recipes_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    all_category = mongo.db.category.find()
    return render_template(
        "view_recipe.html",
        recipes=the_recipe,
        category=all_category)

# editing recipe information
@app.route('/edit_recipe/<recipes_id>', methods=["GET", "POST"])
def edit_recipe(recipes_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
    all_category = mongo.db.category.find()

    return render_template(
        "edit_recipe.html",
        recipe=the_recipe,
        category=all_category,)


# Updating your recipes
@app.route('/update_recipe/<recipes_id>', methods=["POST"])
def update_recipe(recipes_id):
    recipes = mongo.db.recipes
    ingredients = request.form.get('ingredients').splitlines()
    instructions = request.form.get('instructions').splitlines()
    recipes.update({'_id': ObjectId(recipes_id)},
                   {
        # Allows for each new recipe to be given these names and to locate/contain the provided info within the names
        'name': request.form.get('name'),
        'category_name': request.form.get('category_name'),
        'serves': request.form.get('serves'),
        'price': request.form.get('price'),
        'protein': request.form.get('protein'),
        'ingredients': ingredients,
        'instructions': instructions,
        'description': request.form.get('description'),
    })
    return redirect(url_for('index'))

# For deleting recipes
@app.route('/delete_recipe/<recipes_id>', methods=["GET", "POST"])
def delete_recipe(recipes_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipes_id)})
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=os.environ.get("PORT", "5000"),
            debug=False)
