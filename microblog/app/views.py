# -*- coding: utf-8 -*-
from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    # username = {'nickname': 'jayden'}
    # return '''
    # <html>
    #     <head>
    #         <title> Home Page</title>
    #     <head>
    #     <body>
    #         <h1>Hello,''' + username['nickname'] + '''</h1>
    #     </body>
    # </html>
    # '''
    user = {'nickname': 'Jayden'}
    # if control segment
    # return render_template('index.html',
    #                        title='Home',
    #                        user=user)

    # loop control segment
    posts = [
        {'author': {'nickname': 'John'},
         'body': 'Beautiful day in Portland!'
         },
        {'author': {'nickname': 'Susan'},
         'body': 'The Avengers movie was so cool!'}
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
