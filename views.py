from flask import Blueprint, redirect, render_template, request, session, flash, url_for

views=Blueprint('views', __name__)

@views.route('/')
def home_page():
    return render_template("home.html")

@views.route("/admin", methods=["POST", "GET"])
def admin_page():
    password=None
    if "user" in session:
        user=session["user"]
        if request.method=="POST":
            password=request.form.get("pass")
            session["password"]=password
        elif "password" in session:
            password=session["password"]

        return render_template("admin.html", user=user)
    else:
        flash("You are not logged in! ")
        return redirect(url_for("auth.login_page"))

@views.route("/logout") 
def logout():
    if "user" in session:
        session.clear()
        flash("You logged out, not us!", "info")
        return render_template("home.html")
    else:
        flash("You have to log in.", "warning")
        return render_template("login.html")
    
