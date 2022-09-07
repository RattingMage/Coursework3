from flask import Flask, render_template, request, jsonify
from utils import *
import logging

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', filename='logs/api.log')


@app.route("/")
def view_index():
    posts = get_posts_all()
    return render_template("index.html", posts=posts)


@app.route("/api/posts")
def view_api_index():
    logging.info("Запрос /api/posts")
    posts = get_posts_all()
    return jsonify(posts)


@app.route("/api/posts/<int:post_id>")
def view_api_post(post_id):
    logging.info(f"Запрос /api/posts/{post_id}")
    post = get_post_by_pk(post_id)
    return jsonify(post)


@app.route("/post/<int:pid>")
def view_post(pid):
    post = get_post_by_pk(pid)
    comments = get_comments_by_post_id(pid)
    count_comments = good_count_comments(len(comments))
    return render_template('post.html', post=post, comments=comments, count_comments=count_comments)


@app.route("/search", methods=["GET", "POST"])
def view_search():
    query = request.form["search_input"]
    posts = search_for_posts(query)
    return render_template('search.html', count=len(posts), posts=posts)


@app.route("/users/<username>")
def view_users(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts, username=username)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
