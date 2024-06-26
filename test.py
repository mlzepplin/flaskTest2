from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return render_template('index.html', name=name, email=email)
    else:
        return render_template('index.html')


@app.route('/creds/', methods=['GET', 'POST'])
def creds():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return render_template('index.html', name=name, email=email)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)