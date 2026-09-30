from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/home-planner")
def home_planner():
    return render_template("home-planner.html")


@app.route("/jewelry-planner")
def jewelry_planner():
    return render_template("jewelry-planner.html")


@app.route("/party-budget")
def party_budget():
    return render_template("party-budget.html")


if __name__ == "__main__":
    app.run(debug=True)