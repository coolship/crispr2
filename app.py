#!/usr/bin/env python

from flask import Flask
from flask import render_template, redirect, request, url_for, session as flask_session, jsonify
from flask_assets import Environment, Bundle
import simplejson as sjson


app = Flask(__name__,static_url_path='/static')
session = flask_scoped_session(Session, app)


assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle( 'base.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)



@app.route('/')
def index():
    logs = session.query(LineData).order_by(LineData.unixtime).all()
    return render_template("home.html",
                           page={"id":"home"},
                           logs = logs)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5051)
