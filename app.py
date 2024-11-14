from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/exemplo')
def exemplo():
    return render_template('exemplo.html')


if __name__ == '__main__':
    app.run(debug=True)