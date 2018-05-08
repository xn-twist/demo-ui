#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import flash, Flask, render_template, redirect, request, url_for
from xn_twist import XNTwist

app = Flask(__name__)
app.secret_key = 'abc'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/twist", methods=['POST'])
def twist():
    if request.form['domain']:
        domain = request.form['domain']
        return redirect(url_for('results', domain=domain))
    else:
        flash('Please enter a domain.', 'error')
        return redirect(url_for('index'))


@app.route("/<domain>")
def results(domain):
    """."""
    xn = XNTwist()
    results = xn.twist(domain, simple=True)
    return render_template('results.html', domain=domain, possible_squats=results['possible_squats'], count=results['count'])


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
