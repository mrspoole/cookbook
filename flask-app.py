from flask import Flask, render_template, request
#import(yoink) recipe scrapers library
from recipe_scrapers import scrape_me
#Stuff to make python work with html
app = Flask(__name__)

@app.route("/recipe")

def recipe():
    #Tells the scraper where to go
    #Example "https://www.bbcgoodfood.com/recipes/strawberry-ice-cream"
    url = request.args.get("url")
    try:
        #go git it(data)
        scraper = scrape_me(url)
        #All da stuffs we need saved as variables
        return render_template("recipe.html",
            title = scraper.title(),
            ingredients = scraper.ingredients(),
            steps = scraper.instructions_list(),
            image = scraper.image(),
            total_time = scraper.total_time(),
            servings = scraper.yields(),
            error = None
        )
    except Exception as e:
        return render_template("recipe.html",
            error = str(e),
            title = None,
            ingredients = [],
            steps = [],
            image = None,
            total_time = None,
            servings = None
        )
