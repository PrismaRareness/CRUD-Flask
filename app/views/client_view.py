from app import app
from app.forms import client_form
from flask import render_template


@app.route("/register_client")
def register_client():
    form = client_form.ClientForm()
    
    return render_template("clients/form.html", form=form)
