from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["BOOTSTRAP_APP_CONFIG"]
Bootstrap5(app)
ckeditor = CKEditor(app)


class CreateForm(FlaskForm):
    form_title = StringField('Blog Post Title', validators=[DataRequired()])
    form_subtitle = StringField('Subtitle', validators=[DataRequired()])
    form_name = StringField("Your Name", validators=[DataRequired()])
    form_img = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    form_content = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField('SUBMIT POST')


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=["GET", "POST"])
def create_post():
    form = CreateForm()
    today = datetime.today()
    formatted_date = today.strftime("%B %d, %Y")
    if form.validate_on_submit():
        new_blog = BlogPost(
            title=form.form_title.data,
            subtitle=form.form_subtitle.data,
            date=formatted_date,
            body=form.form_content.data,
            author=form.form_name.data,
            img_url=form.form_img.data
        )
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form)


# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    edit_form = CreateForm(
        form_title=post.title,
        form_subtitle=post.subtitle,
        form_img=post.img_url,
        form_name=post.author,
        form_content=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.form_title.data
        post.subtitle = edit_form.form_subtitle.data
        post.body = edit_form.form_content.data
        post.author = edit_form.form_name.data
        post.img_url = edit_form.form_img.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post.id))

    return render_template('make-post.html', form=edit_form, is_edit=True)


# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<int:post_id>', methods=['GET', 'POST'])
def delete_post(post_id):
    post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    db.session.delete(post)
    db.session.commit()
    return redirect("url_for('get_all_posts')")


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
