from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/1.html')
def page_1():
    return render_template('1.html')

@app.route('/bye')
def bye():
    return '<p>bye</p>'

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('fname')
    if name:
        return redirect(url_for('welcome', name=name))
    return redirect(url_for('home'))


@app.route('/<name>')
def welcome(name):
    return f'{name}, welcome back'



if __name__ == '__main__':
    app.run(debug=True)
