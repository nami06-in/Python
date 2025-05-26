"""
    MAKE POST REQUESTS WITH FLASK AND HTML FORMS

"""

from flask import Flask, render_template, request
from send_email import Mail
import requests

# USE YOUR OWN npoint LINK! 👇
posts = requests.get("https://api.npoint.io/bbab6fcdfd88f4837f2a").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    else:
        data = request.form
        email_addr = data['email']
        message = (f"Name: {data['name']}\nEmail: {data['email']}\n"
                   f"Phone: {data['phone']}\nMessage: {data['message']}")
        mail = Mail(email_addr, message)
        mail.send_mail()
        return render_template("contact.html", message_send=True)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
