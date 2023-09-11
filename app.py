
from flask import Flask, render_template, request, redirect, flash, url_for
import pickle
from os import environ


app = Flask(__name__)
app.secret_key = "mywebsite2023"


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/health_test', methods=["POST", "GET"])
def health_test():
    if request.method == "POST":
        datapts = request.form.values()
        formatted = [x for x in datapts]
        features = [int(x) for x in formatted[1:]]

        model = pickle.load(open('./MHSModel.pkl', 'rb'))
        predictions = model.predict([features])

        if predictions[0] == 0:
            flash("You don't need treatment!", 'success')
        else:
            flash("You need treatment!", 'error')

    return render_template('health_test.html')


if __name__ == "__main__":
    app.run(debug=True)
