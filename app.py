from flask import Flask, render_template, request, redirect, url_for, flash
from flask_migrate import Migrate
from db import db
from models import User
from config import Config
from flask_socketio import SocketIO, emit
import json
from flask import make_response

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

is_successfull = False
name = ''
phoneNo = ''
@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/rescue",methods=['GET','POST'])
def rescue():
    return render_template("rescue.html")

@app.route("/submit_rescue", methods=['POST'])
def submit_rescue():
    global name
    global phoneNo

    name = request.form['name']
    phoneNo = request.form['phoneNo']
    print("Type of name:",type(name))

    return "Form submitted"

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

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        global is_successfull
        organization_email = request.form['organization_email']
        password = request.form['password']
        user = User.query.filter_by(organization_email=organization_email).first()
        
        if user:
            if user.password == password:
                flash('Login successful!', 'success')
                is_successfull = True
                return redirect(url_for('organization'))  # Redirect to organization route after successful login
            else:
                is_successfull = False
                flash('Invalid password, please try again.', 'danger')
        else:
            is_successfull = False
            flash('Login failed. Check your organization email and password.', 'danger')
    
    return render_template("login.html")


# @app.route("/organization")
# def organization():
#     return render_template("organization.html", name=name, phone_no=phoneNo)

@app.route('/organization')
def organization():
    # response = make_response(render_template('organization.html', name=name, phone_no=phoneNo))
    # response.headers['Cache-Control'] = 'no-store'
    if is_successfull == False:
        return render_template("login.html")
    else:
        return render_template("organization.html")

@app.route("/precautions")
def precaution():
    return render_template("precautions.html")

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        organization_name = request.form['organization_name']
        organization_email = request.form['organization_email']
        password = request.form['password']
        confirm_password = request.form['re_password']

        # Check if passwords match
        if password != confirm_password:
            flash('Password and confirm password do not match.', 'danger')
            return redirect(url_for('signup'))

        # Check if user already exists
        existing_user = User.query.filter_by(organization_name=organization_name).first()
        if existing_user:
            flash('Organization name already exists. Please choose a different one.', 'danger')
            return redirect(url_for('signup'))

        # Check if email already exists
        existing_email = User.query.filter_by(organization_email=organization_email).first()
        if existing_email:
            flash('Email already exists. Please use a different email.', 'danger')
            return redirect(url_for('signup'))

        # Create new user
        new_user = User(organization_name=organization_name, organization_email=organization_email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Signup successful!', 'success')
        return redirect(url_for('login'))

    return render_template("signup.html")

@socketio.on('send_location')
def handle_message(data):
    print("Data type: ", type(data))
    dataString = data.encode('utf-8')
    parsed_data = json.loads(dataString)
    emit('receive_location', json.dumps(parsed_data), broadcast=True)

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=4000, debug=True)
    socketio.run(app, host='0.0.0.0',debug=True)
