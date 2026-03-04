from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response=requests.get('https://api.npoint.io/63647823939b1f24402a')
    blog_posts=response.json()
    return render_template("index.html", blog_posts=blog_posts)
@app.route('/blogs/<int:num>')
def data(num):
    response = requests.get('https://api.npoint.io/63647823939b1f24402a')
    blog_posts = response.json()
    found_post=None
    for blogs in blog_posts:
        if blogs["id"]==num:
            found_post=blogs
            return render_template("post.html", post=found_post)
if __name__ == "__main__":
    app.run(debug=True,port=8080)
