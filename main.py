from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def get_inside(name, password):
    return render_template("enter.html")



if __name__ == "__main__":
    app.run(debug=True)

