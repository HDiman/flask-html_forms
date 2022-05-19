from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    get_username = request.form['username']
    get_password = request.form['password']
    return render_template('login.html', username=get_username, password=get_password)


if __name__ == "__main__":
    app.run(debug=True)

