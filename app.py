from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/abouts')
def abouts():
    return render_template('abouts.html')

# @app.route('/ideas')
# def ideas():
#     return render_template('ideas.html')

# @app.route('/builds')
# def builds():
#     return render_template('builds.html')

# @app.route('/tools')
# def tools():
#     return render_template('tools.html')

# Testing Pages
@app.route('/templates')
def templates():
    return render_template('templates.html')

if __name__ == '__main__':
    app.debug = True
    app.run()