from flask import abort, render_template

def index():
    return render_template("dashboard.html")