from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/rescue.html")
def rescue():
    return render_template("rescue.html")

@app.route("/about-us.html")
def about_us():
    return render_template("about-us.html")

@app.route("/Blog.html")
def blog():
    return render_template("Blog.html")

@app.route("/emergency.html")
def emergency():
    return render_template("emergency.html")

@app.route("/gallery.html")
def gallery():
    return render_template("gallery.html")

@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/organization.html")
def organization():
    return render_template("organization.html")

@app.route("/precautions.html")
def precaution():
    return render_template("precautions.html")

@app.route("/signup.html")
def signup():
    return render_template("singup.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)