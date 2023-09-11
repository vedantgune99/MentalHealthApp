
from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
from config import emailID, password, SECRET_KEY
import pickle


app = Flask(__name__)
app.secret_key = SECRET_KEY

# configuration of mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = emailID
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        req = request.form
        collected = [x for x in req.values()]
        user_name = collected[0]
        user_email = collected[1]
        user_message = collected[2]

        msg = Message(
            'Support Required',
            sender=emailID,
            recipients=[user_email]
        )
        msg.body = f'''
            Name : {user_name}
            Email : {user_email}
            Message : {user_message}
            Dear {user_name},
                    Welcome, Your issue will be resolved as soon as possible, we will contact you back soon!
                    \nThank You!
            '''
        mail.send(msg)
        flash("Query sent successfully!", 'success')
        return redirect(url_for('homepage'))

    return render_template('contact.html')


@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/health_test', methods=["GET", "POST"])
def health_test():
    try:
        if request.method == "POST":
            datapts = [int(x) for x in request.form.values() if x.isdigit()]
            if not datapts:
                flash('Invalid input. Please enter numeric values.', 'error')
            else:
                model_loaded = pickle.load(open('./MHSModel.pkl', 'rb'))
                prediction = model_loaded.predict([datapts])

                if prediction[0] == 0:
                    flash('Your test results are negative!', 'success')
                    return redirect(url_for('health_test'))

                else:
                    flash(
                        'Your test results are positive. Please see a good Psychiatrist!', 'error')
                    return redirect(url_for('support'))
        else:
            return render_template('health_test.html')

    except Exception as e:
        flash("An error occurred: " + str(e), 'error')
        return redirect(url_for('health_test'))


if __name__ == "__main__":
    app.run(debug=True)
