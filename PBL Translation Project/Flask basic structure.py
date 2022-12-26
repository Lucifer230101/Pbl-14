from flask import Flask, redirect, url_for, request, render_template


#initialize wsgi application
app = Flask(__name__)

# render templates
@app.route('/')
def Index():
    return render_template("Index.html")

@app.route("/pass/<int:score>")
def Pass(score):
    return render_template("pass.html", marks=score)

@app.route("/fail/<int:score>")
def Fail(score):
    return render_template("fail.html", marks=score)

@app.route("/result/<int:marks>")
def result(marks):
    final_result = ""
    if marks<35:
        final_result = "Fail"
    else:
        final_result = "Pass"
    return redirect(url_for(final_result, score = marks))

@app.route("/submit", methods=["POST","GET"])
def submit():
    total_score = 0
    if request.method=="POST":
        science_marks = float(request.form["science"])
        maths_marks = float(request.form["maths"])
        history_marks = float(request.form["history"])
        english_marks = float(request.form["english"])
        avg_marks = (science_marks + maths_marks + history_marks + english_marks)/4
    if avg_marks <35:
        return redirect(url_for("Fail", score = avg_marks))
    else:
        return redirect(url_for("Pass", score = avg_marks))






# run the application
if __name__ == "__main__":
    app.run(debug=True)