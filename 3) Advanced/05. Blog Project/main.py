"""
     TEMPLATING WITH JINJA IN FLASK APPLICATIONS
"""


from flask import Flask, render_template
from post import Post


app = Flask(__name__)
blog_posts = Post()


@app.route('/')
def home():
    return render_template("index.html", posts=blog_posts.all_posts)


@app.route('/post/<int:post_id>')
def read(post_id):
    return render_template("post.html", id=post_id, posts=blog_posts.all_posts)


if __name__ == "__main__":
    app.run(debug=True)
