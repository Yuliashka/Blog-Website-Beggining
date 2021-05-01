# CREATING OF A FAKE BLOG: https://www.npoint.io/docs/5abcca6f4e39b4955965

from flask import Flask, render_template
from post import Post
import requests

# GETTING INFO FROM FAKE BLOG WEBSITE:
posts = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
# creating a list
post_objects = []
for post in posts:
    # creating an object from Post class (post.py):
    # в него передаем данные о нашем id из каждого поста, субтайтл, основной текст
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


app = Flask(__name__)

# CREATING A HOME PAGE:
@app.route("/")
def home():
    return render_template('index.html', posts=post_objects)

# CREATING A POST PAGE:
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)