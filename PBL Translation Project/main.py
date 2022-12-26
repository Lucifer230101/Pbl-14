from flask import Flask, render_template, redirect, url_for, request
import pickle


# initialize wsgi app
app = Flask(__name__, template_folder="Templates", static_folder="Static")


@app.route("/")
def home():
    return render_template("Home.html")


@app.route("/pricing")
def pricing():
    return render_template("Pricing.html")


@app.route("/contact")
def contact():
    return render_template("Contact.html")


@app.route("/about")
def result():
    return render_template("About.html")


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        input_sentence = request.form["input_sentence"]
        with open("Eng_Mar_Translator.pkl", "rb") as f:
            model = pickle.load(f)
            output_sentence = model.predict(input_sentence)
            return render_template("Home.html", data=output_sentence)
        # -----------------------------------------------------------
        # user_selection = request.form["select_language"]
        # input_sentence = request.form["input_sentence"]
        # if user_selection == 1:
        #     # model = pickle.load("Eng_to_mar.pkl")
        #     # output_sentence = model.predict(input_sentence)
        #     output_sentence = "success1"
        # elif user_selection == 2:
        #     # model = pickle.load("Mar_to_Eng.pkl")
        #     # output_sentence = model.predict(input_sentence)
        #     output_sentence = "success2"
        # return redirect(url_for("result"))
        # ------------------------------------------------------------


@app.route("/Contact/submit", methods=["POST", "GET"])
def contact_submit():
    if request.method == "POST":
        return render_template("Contact_Thank_page.html")


if __name__ == "__main__":
    app.run(debug=True)
