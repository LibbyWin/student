import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'StudentLife'
app.config["MONGO_URI"] = 'mongodb+srv://LWin_01:01Libby@StudentLife-ldsrb.mongodb.net/StudentLife?retryWrites=true&w=majority'
                                    
mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    recipes=mongo.db.recipes.find()
    categories=mongo.db.categories.find()
    return render_template("index.html", recipes=recipes, categories=categories,)




@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html", page_title="Add Recipe", 
    recipes=mongo.db.recipes.find(),
    categories=mongo.db.categories.find())




@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes=mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('index'))



@app.route('/view_recipe/<recipes_id>')
def view_recipe(recipes_id):
   the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipes_id)})
   all_category = mongo.db.category.find() 

   return render_template("view_recipe.html", recipes=the_recipe, category=all_category)





if __name__ == "__main__":  
        app.run(host=os.environ.get("IP"),
        port=os.environ.get("PORT"),
        debug=True)