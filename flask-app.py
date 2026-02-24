from flask import Flask, render_template, request
from recipe_scrapers import scrape_me

app = Flask(__name__)

@app.route("/recipe")
def recipe():
    url = request.args.get("url")
    try:
        scraper = scrape_me(url)
        return render_template("recipe.html",
            title = scraper.title(),
            image = scraper.image(),
            total_time = scraper.total_time(),
            yields = scraper.yields(),
            ingredients = scraper.ingredients(),
            instructions = scraper.instructions_list(),
            error = None
        )
    except Exception as e:
        return render_template("recipe.html",
            error = str(e),
            title = None,
            image = None,
            total_time = None,
            yields = None,
            ingredients = [],
            instructions = []
        )
