from flask import Flask, render_template

#Initialize the app
app = Flask(__name__)


# home route
@app.route("/")
def home():
    return render_template("home.html")


# signup route
@app.route("/signup")
def signup():
    return render_template("signup.html")


# signin route
@app.route("/signin")
def signin():
    return render_template("signin.html")


if __name__ == "__main__":
    app.run(debug=True) 
    