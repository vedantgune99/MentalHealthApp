from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)


@app.route('/')
def homepage():
    # return "Hello, World!"
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/health_test', methods=['POST', 'GET'])
def health_test():
    '''
    datapts = []
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        se = request.POST.get('se')
        fh = request.POST.get('fh')
        wi = request.POST.get('wi')
        noe = request.POST.get('noe')
        rw = request.POST.get('rw')
        tc = request.POST.get('tc')
        b = request.POST.get('b')
        co = request.POST.get('co')
        wp = request.POST.get('wp')
        sh = request.POST.get('sh')
        a = request.POST.get('a')
        l = request.POST.get('l')
        mhc = request.POST.get('mhc')
        phc = request.POST.get('phc')
        c = request.POST.get('c')
        s = request.POST.get('s')
        mhi = request.POST.get('mhi')
        phi = request.POST.get('phi')
        mvp = request.POST.get('mvp')
        oc = request.POST.get('oc')

        datapts = [age, gender, se, fh, wi, noe, rw, tc, b, co,
                   wp, sh, a, l, mhc, phc, c, s, mhi, phi, mvp, oc]

        data = [int(x) for x in datapts]

        model_loaded = pickle.load(open('Extras/MHSModel.pkl', 'rb'))
        prediction = model_loaded.predict([data])

        if (prediction[0] == 0):
            messages.add_message(request, messages.SUCCESS,
                                 "Your test results are Negetive!")
            return redirect('/')

        else:
            messages.add_message(
                request, messages.ERROR, "Your test results are Positive, Please see a good Psychiatrist!")
            return redirect('/gethelp')

    return render(request, 'mhtest.html')

    return render_template('health_test.html')
    '''


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/support')
def support():
    return render_template('support.html')


if __name__ == "__main__":
    app.run(debug=True, port=3000)
