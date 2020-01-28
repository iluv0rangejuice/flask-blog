from app import app
from markdown import markdown, request
from flask import render_template_string
from helpers import render_markdown

#safe global import (okay to use)
import flask

#global import (try to avoid)
#from flask import *

'''
#Old way to open files
html_file = open('app/views/index.html')
html_file = html_file.read()
html_file.close()
return html_file

#New way (safer and easier //more recommned way to use in python)
html = ""
with open('app/views/index.md') as html_file:
    html = html_file.read()
    html = markdown(html)
return html
'''
#home page
@app.route("/")
def home():
    return render_markdown('index.md')

#general page
@app.route("/general")
def about():
    html = ""
        with open('app/views/about.md') as html_file:
        html = html_file.read()
        html = markdown(html)
    return html
    return "<h1>About Me<h1>"

#generic page
@app.route("/<view_name>")

#input parameter name must match route parameter
def render_page(view_name):
    html = render_markdown(view_name + '.md')
    return render_template_string(html, view_name = view_name)


#contact page
@app.route("/contact")
def about():
    return render_markdown('contact.md')

#login page
@app.route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #TODO: process request.value as necessary
        pass