from flask import Flask, render_template
from flask import request, redirect, flash, url_for

import pickle


app = Flask(__name__)
app.secret_key = "MHS_APP123"


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/health_test', methods=["GET", "POST"])
def health_test():
    datapts = []
    try:
        if request.method == "POST":
            req = request.form
            for x in req.values():
                datapts.append(x)

            datapts = [int(x) for x in datapts[1:]]

            model_loaded = pickle.load(open('MHSModel.pkl', 'rb'))
            prediction = model_loaded.predict([datapts])

            if (prediction[0] == 0):
                flash('Your test results are negetive!', 'success')
                return redirect(url_for('homepage'))

            else:
                flash(
                    "Your test results are Positive, Please see a good Psychiatrist!", 'error')
                return redirect(url_for('support'))

        else:
            return render_template('health_test.html')

    except Exception as e:
        flash("An error occurred!", 'error')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/support')
def support():
    return render_template('support.html')


if __name__ == "__main__":
    app.run(debug=False, port=8080)
