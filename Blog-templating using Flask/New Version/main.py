from flask import Flask, render_template
app = Flask(__name__)
import requests
from datetime import datetime
date=datetime.now().year
response=requests.get('https://api.npoint.io/2b798c65cc4f354a4662')
blogs=response.json()
requested_posts=blogs

@app.route('/')
def index():
    return render_template("index.html",blog_posts=requested_posts)

@app.route("/about")
def about():
    return render_template("about.html",date=date)

@app.route("/post/<int:post_id>")
def post(post_id):
    return render_template("post.html",blog_posts=requested_posts,date=date,num=post_id)
@app.route("/contact")
def contact():
    return render_template("contact.html",date=date)


if __name__ == '__main__':
    app.run(debug=True,host="localhost", port="8080")