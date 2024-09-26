from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
from textblob import TextBlob
from transformers import pipeline

api = "AIzaSyBrSRQOusWyAMBfm1F27g6Ci97xk5-J258"
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def landing():
    if request.method == "POST":
        username = request.form.get("username")
        return redirect(url_for("index", username=username))
    return render_template("landing.html")

@app.route("/index", methods=["GET", "POST"])
def index():
    username = request.args.get("username")
    return render_template("index.html", username=username)

@app.route("/financial_FAQ", methods=["GET", "POST"])
def financial_FAQ():
    return render_template("financial_FAQ.html")

@app.route("/makersuite", methods=["GET", "POST"])
def makersuite():
    q = request.form.get("q")
    response = model.generate_content(q)
    return render_template("makersuite.html", r=response.text)

@app.route("/joke", methods=["GET", "POST"])
def joke():
    joke_text = "Which noodle is the heaviest? Wanton (one-tonne) noodles."
    return render_template("joke.html", joke=joke_text)

@app.route("/textblob_analysis", methods=["POST"])
def textblob_analysis():
    text = request.form.get("text")
    analysis = TextBlob(text).sentiment
    return render_template("textblob_result.html", text=text, analysis=analysis)

if __name__ == "__main__":
    app.run()
