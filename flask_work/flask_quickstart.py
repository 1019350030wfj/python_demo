# -*- coding:utf-8 -*-

from flask import Flask, url_for, make_response, render_template, jsonify
import json

app = Flask(__name__)


@app.route('/project/')
def project():
    return 'Project'


@app.route('/about')
def about():
    return '谢谢大神访问！！！' + url_for('project')+url_for('static', filename='style.css')


@app.route('/test_cookie')
def test_cookie():
    resp = make_response(render_template('test_cookie.html'))
    resp.set_cookie('username', "jayden")
    return resp


@app.route('/test_cookie_json')
def test_cookie_json():
    resp = make_response(jsonify(status=200,
                       info='jayden',
                       msg='success'))
    resp.set_cookie('username', "jayden_wsy")
    return resp




if __name__ == '__main__':
    app.run(debug=True)
