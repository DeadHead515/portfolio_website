from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/posts/')
def blog_p():
    return 'Blog post will go here.'

if __name__ == '__main__':
    app.run(debug=True)