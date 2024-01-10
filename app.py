from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/rescue")
def rescue():
    return render_template("rescue.html")

@app.route("/about-us")
def about_us():
    return render_template("about-us.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/emergency")
def emergency():
    return render_template("emergency.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/organization")
def organization():
    return render_template("organization.html")

@app.route("/precautions")
def precaution():
    return render_template("precautions.html")

@app.route("/signup")
def signup():
    return render_template("singup.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4000, debug=True)