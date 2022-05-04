from flask import Flask, render_template, request
from password import validate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def promt_password():
  if request.method == "POST":
    password = request.form['password']
    if validate(password):
      return "Welcome"
    else:
      return "Wrong password"
  return render_template('prompt_password.html')
