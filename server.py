from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'on top of spaghetti'

@app.route('/')
def index():
    session['counter'] = 1
    return render_template('index.html', counter=session['counter'])

@app.route('/clear', methods=['POST'])
def clear():
    session['counter'] = 1
    return render_template('index.html', counter=session['counter'])

@app.route('/counter_post', methods=['POST'])
def counter_post():
    session['counter'] += 1
    return redirect('/show_counter')

@app.route('/counter_post2', methods=['POST'])
def counter_post2():
    session['counter'] += 2
    return redirect('/show_counter')

@app.route('/show_counter')
def show_counter():
    return render_template('show.html', counter=session['counter'])

if __name__ == '__main__':
    app.run(debug=True)