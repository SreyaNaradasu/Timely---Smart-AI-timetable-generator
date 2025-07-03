from flask import Flask, render_template, request
from scheduler import generate_timetable, time_slots

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    timetable = {}
    semester = ''
    section = ''
    if request.method == "POST":
        semester = request.form["semester"]
        section = request.form["section"]
        timetable = generate_timetable(semester, section)
    return render_template("index.html", semester=semester, section=section, timetable=timetable, time_slots=time_slots)

if __name__ == "__main__":
    app.run(debug=True)
