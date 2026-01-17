from flask import Flask, render_template, request
from data_store import save_waste_data
from dashboard_logic import create_graphs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        waste_type = request.form.get("waste_type")
        area = request.form.get("area")

        
        if waste_type == "Plastic":
            impact = "RED"
        elif waste_type == "Paper":
            impact = "YELLOW"
        else:
            impact = "GREEN"

        save_waste_data(area, waste_type, impact)

    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    create_graphs()
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
