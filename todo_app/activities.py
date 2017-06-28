from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
import http.server 
import os

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def homepage():
       return render_template('portifolio.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4450))
    app.debug = False
    app.run(host='0.0.0.0', port=port)