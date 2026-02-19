from flask import Blueprint, redirect, render_template, request, session, flash, url_for
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from Flasky import db

auth=Blueprint('auth', __name__)

@auth.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        session.permanent = True
        user=request.form.get("nm")
        password=request.form.get("pass")
        session["user"]=user
        session["password"]=password
        user=User.query.filter_by(name=user).first()
        if user:
            if check_password_hash(user.password, password):
                return redirect(url_for("views.admin_page"))
            else:
                flash("Wrong Password! ")
                return render_template("login.html")
        else:
            flash("User does not exist! ")
            return render_template("login.html")
        
    else:
        return render_template("login.html")
    
@auth.route("/reset")
def reset_page():
    return render_template("reset.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        user=request.form.get("nm")
        password=request.form.get("pass")
        new_user=User(name=user, password=generate_password_hash(password))
        user= User.query.filter_by(name=user).first()
        if user:
            flash("User already exists")
            return redirect(url_for("auth.login_page"))

        else:
            db.session.add(new_user)
            db.session.commit()
            flash("Account Successfully Created!")
            return redirect(url_for('auth.login_page'))
    else:
        return render_template("signup.html")