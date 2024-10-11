from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def inicial():
    return render_template('template.html')

@app.route('/exemplo')
def exemplo():
    return render_template('exemplo.html')

@app.route('/exercicio')
def exercicio():
    return render_template('exercicio.html')

@app.route('/exercicio_1')
def exercicio_1():
    return render_template('exercicio_1.html')

@app.route('/exercicio_2')
def exercicio_2():
    return render_template('exercicio_2.html')

@app.route('/exercicio_3')
def exercicio_3():
    return render_template('exercicio_3.html')

@app.route('/exercicios_4')
def exercicio_4():
    return render_template('exercicio_4.html')



if __name__ == '__main__':
    app.run(debug=True)