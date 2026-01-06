from flask import Flask, render_template
from helpers import generate_plan
from database import get_recent_plans, save_plan
from database import init_db

import json
import os

#from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
#from flask_session import Session
#from tempfile import mkdtemp
#from werkzeug.security import check_password_hash, generate_password_hash
#import datetime

app = Flask(__name__)
init_db()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    
@app.route("/faq", methods=["GET", "POST"])
def faqs():
    if request.method == "GET":
        return render_template("faq.html")
    
@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return render_template("about.html")
    
@app.route("/result", methods=["POST"])
def result():
    lesson_names = request.form.getlist("lesson_name")
    scores = request.form.getlist("score")

    total_score = int(request.form.get("total_score"))

    free_time = request.form.get("free_time")

    lessons = []
    for name, score in zip(lesson_names, scores):

        lessons.append({
            "name": name,
            "score": int(score),
            "total_score": total_score
        })

    plan = generate_plan(lessons, free_time)
    save_plan(free_time, plan)

    return render_template("result.html", plan=plan)

@app.route("/history", methods = ["GET"])
def history():
    rows = get_recent_plans()

    plans = []
    for row in rows:
        plans.append({
            "id": row[0],
            "created": row[1],
            "free_time": row[2],
            "lessons": json.loads(row[3])
        })

    return render_template("history.html", plans=plans)

if __name__ == "__main__":
    app.run(debug=True)
