import os
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def main():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not content:
            flash('Content is required!')
        else:
            return redirect(url_for('result'))
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
