import requests

# BLOG_API = "https://api.npoint.io/c790b4d5cab58020d391"
BLOG_API = "https://api.npoint.io/638a88052de3f968175a"


class Post:
    def __init__(self):
        self.response = requests.get(BLOG_API)
        self.all_posts = self.response.json()
