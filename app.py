from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
from textblob import TextBlob
from transformers import pipeline

# Google Generative AI configuration
api = "AIzaSyBrSRQOusWyAMBfm1F27g6Ci97xk5-J258"
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize Flask app
app = Flask(__name__)

# Landing page route
@app.route("/", methods=["GET", "POST"])
def landing():
    if request.method == "POST":
        username = request.form.get("username")
        # Redirect to the index page with the username as a query parameter
        return redirect(url_for("index", username=username))
    return render_template("landing.html")

# Index route with username as a query parameter
@app.route("/index", methods=["GET", "POST"])
def index():
    username = request.args.get("username")
    return render_template("index.html", username=username)

# Financial FAQ route
@app.route("/financial_FAQ", methods=["GET", "POST"])
def financial_FAQ():
    return render_template("financial_FAQ.html")

# Makersuite route for Google Generative AI content
@app.route("/makersuite", methods=["GET", "POST"])
def makersuite():
    q = request.form.get("q")
    response = model.generate_content(q)
    return render_template("makersuite.html", r=response.text)

# Singapore joke route
@app.route("/joke", methods=["GET", "POST"])
def joke():
    joke_text = "Which noodle is the heaviest? Wanton (one-tonne) noodles."
    return render_template("joke.html", joke=joke_text)

# TextBlob sentiment analysis route
@app.route("/textblob_analysis", methods=["POST"])
def textblob_analysis():
    text = request.form.get("text")
    analysis = TextBlob(text).sentiment
    return render_template("textblob_result.html", text=text, analysis=analysis)

if __name__ == "__main__":
    app.run()
