from flask import Flask

app = Flask(__name__)
print(__name__)  # __main__ will be printed


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_italics(function):
    def wrapper():
        return f"<i>{function()}</i>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"

    return wrapper


@app.route('/')  # / is given to go to the home page
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a Paragraph</p>' \
           '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXhkYnA3dnU0M3kwbmNkd21pZmhkbjMwM3JuNTJyems4M3o4NjZnNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9dg/cwQCUhKible5mGrtMO/giphy.gif" width=200>'


@app.route('/bye')  # app is an object created at the begining and rout() is a function of Flask
@make_bold
@make_italics
@make_underlined
def say_bye():
    return "Bye"  # Go to http://127.0.0.1:5000/bye


@app.route('/username/<name>/<int:number>')  # '/<name>' is also correct, but you need to stop and rerun the server
# otherwise it gives an error
def greet(name, number):
    return f"Hello there, {name}. You are {number}years old!"


# To run without using the terminal:-
if __name__ == '__main__':
    app.run(debug=True)  # To turn on debugger mode
