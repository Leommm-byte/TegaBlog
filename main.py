from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)


blog_endpoint = "https://api.npoint.io/919f5e765a594efbd37e"
blog_details = requests.get(blog_endpoint).json()


@app.route("/")
def home():
    return render_template("index.html", details=blog_details)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:num>")
def get_post(num):
    requested_post = None
    for blog in blog_details:
        if blog["id"] == num:
            requested_post = blog

    return render_template("post.html", post=requested_post, image=requested_post["image_url"])


if __name__ == "__main__":
    app.run(debug=True)

