# .py
from flask import Flask, render_template, request
from gpt_prompts import get_agro_advice

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    advice = None
    if request.method == "POST":
        crop = request.form["crop"]
        advice = get_agro_advice(crop)
    return render_template("index.html", advice=advice)

if __name__ == "__main__":
    app.run(debug=False)
