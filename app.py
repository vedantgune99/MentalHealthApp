
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
    try:
        if request.method == "POST":
            print(request.method)
            datapts = [int(x) for x in request.form.values() if x.isdigit()]
            if not datapts:
                flash('Invalid input. Please enter numeric values.', 'error')
            else:
                model_loaded = pickle.load(open('./MHSModel.pkl', 'rb'))
                prediction = model_loaded.predict([datapts])
                if prediction[0] == 0:
                    flash('Your test results are negative!', 'success')
                else:
                    flash(
                        'Your test results are positive. Please see a good Psychiatrist!', 'error')
            return redirect(url_for('health_test'))
        else:
            return render_template('health_test.html')
    except Exception as e:
        flash("An error occurred: " + str(e), 'error')


if __name__ == "__main__":
    app.run(debug=True)
