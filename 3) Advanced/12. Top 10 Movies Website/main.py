from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

import os
from dotenv import load_dotenv

load_dotenv()


MOVIE_URL = "https://api.themoviedb.org/3/search/movie"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"
MOVIE_DB_API_KEY = os.environ["MOVIE_DB_API_KEY"]

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["BOOTSTRAP_APP_CONFIG"]
Bootstrap5(app)


class UpdateForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
# Create the extension
db = SQLAlchemy(model_class=Base)
# initialise the app with the extension
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


# new_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family ("
#                 "Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each "
#                 "other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()  # convert ScalarResult to Python List
    print(all_movies)

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def update():
    form = UpdateForm()
    movie_id = request.args.get('id')  # this id is retrieved from index.html
    movie_selected = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie_selected.rating = form.rating.data
        movie_selected.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie_selected)


@app.route('/delete', methods=["GET", "POST"])
def delete():
    movie_id = request.args.get('id')  # this id is retrieved from index.html
    movie_selected = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_selected)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie = form.title.data
        response = requests.get(MOVIE_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie})
        data = response.json()['results']
        return render_template('select.html', options=data)
    return render_template('add.html', form=form)


@app.route('/find')
def find():
    movie_id = request.args.get('id')
    movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
    data = response.json()
    print(data)
    new_movie = Movie(
        title=data['title'],
        year=data['release_date'].split('-')[0],
        description=data['overview'],
        img_url=f"{IMAGE_URL}{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('update', id=new_movie.id))


if __name__ == '__main__':  # Comment these 2 line if integrity error is found
    app.run(debug=True)
