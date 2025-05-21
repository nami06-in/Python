class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):   #  *args - The new_user passed by the create_blog_post in the 21st line.
        if args[0].is_logged_in == True:  # Here the new_user object is the first argument.
            function(args[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("angela")
new_user.is_logged_in = True

another_user = User("Namitha")

last_user = User("Maria")
last_user.is_logged_in = True

create_blog_post(new_user)
create_blog_post(another_user)
create_blog_post(last_user)
