from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'on top of spaghetti'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/counter_post', methods=['POST'])
def counter_post():
    return redirect('/show_counter')

@app.route('/show_counter')
def show_counter():
    return render_template('show.html')

if __name__ == '__main__':
    app.run(debug=True)