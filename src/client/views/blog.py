import json

from flask import Blueprint, render_template, request, session

blog_bp = Blueprint('blog', __name__, template_folder='templates')


@blog_bp.route('/blog/<page_no>')
def blog(page_no):
    """ REST endpoint for the blog dashboard. """
    with open('json/blogs.json') as blogs:
        blogs = json.load(blogs)
    blogs_split = {}
    pg = 1
    blog_pgs = []
    for i in range(0, len(blogs.items()), 3):
        blog_pgs.append(pg)
        for blog in list(blogs.items())[i:i+3]:
            if pg in blogs_split.keys():
                blogs_split[pg].append(blog)
            else:
                blogs_split[pg] = [blog]
        pg = pg + 1
    return render_template('blog_dashboard.html', title='Blog', blogs=blogs_split[int(page_no)], page_no=int(page_no), 
            blog_pgs=blog_pgs)

