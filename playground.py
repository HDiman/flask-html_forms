from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    # return render_template('login.html', username=username, password=password)
    return redirect(url_for('login', username=username, password=password)) # then you can pass email or pass


if __name__ == "__main__":
    app.run(debug=True)

