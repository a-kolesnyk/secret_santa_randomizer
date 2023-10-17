# app.py

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/generate_pairs", methods=["POST"])
def generate_pairs():
  names = request.form.getlist("name")

  random.shuffle(names)
  pairs = [(names[i], names[(i + 1) % len(names)]) for i in range(len(names))]

  return render_template("pairs.html", pairs=pairs)

if __name__ == "__main__":
  app.run(debug=True)
