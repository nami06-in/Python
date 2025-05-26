from flask import Flask, render_template
import requests

# BLOG_URL = "https://api.npoint.io/15eb84cecc4c9da76ff2"
BLOG_URL = "https://api.npoint.io/bbab6fcdfd88f4837f2a"
blog_data = requests.get(BLOG_URL).json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template('index.html', all_posts=blog_data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return render_template("post.html", id=post_id, posts=blog_data)


if __name__ == '__main__':
    app.run(debug=True)
