import requests
from flask import Flask, render_template, redirect, url_for, request
import waitress
import os,json

app = Flask(__name__)

@app.route('/')

def trending():
	msg={"message":"Hello from the other side"}
	return json.dumps(msg)


if __name__ == "__main__":
     app.debug = False
     port = int(os.environ.get('PORT', 33507))
     waitress.serve(app, port=port)