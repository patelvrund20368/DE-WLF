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

@app.route("/Blog")
def blog():
    return render_template("Blog.html")

@app.route("/emergency")
def emergency():
    return render_template("emergency.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
    return render_template("organization.html")

@app.route("/organization")
def organization():
    return render_template("organization.html")

@app.route("/precautions")
def precaution():
    return render_template("precautions.html")

<<<<<<< HEAD
@app.route("/signup", methods=['post', 'get'])
=======
@app.route("/signup", methods=['POST', 'GET'])
>>>>>>> 3074b10f1f5fa34cf4349b12a8d59a5172e43911
def signup():
    return render_template("organization.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4000, debug=True)