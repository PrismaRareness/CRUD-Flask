from app import app, db
from app.forms import client_form
from app.models import client_model
from flask import redirect, render_template, url_for


@app.route("/register_client", methods=['GET', 'POST'])
def register_client():
    form = client_form.ClientForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        birth_date = form.birth_date.data
        occupation = form.occupation.data
        gender = form.gender.data
        
        client = client_model.Client(name=name, email=email, 
                                     birth_date=birth_date, occupation=occupation, 
                                     gender=gender)
        try:
            db.session.add(client)
            db.session.commit()
            return redirect(url_for("Listar_clientes"))
        except:
            print("Cliente não cadastrado")    

    return render_template("clients/form.html", form=form)

@app.route("/clients_list", methods=["GET"])
def clients_list():
    clients = client_model.Client.query.all()
    return render_template("clients/clients_list.html", clients=clients)

@app.route("/client_list/<int:id>")
def clients_list():
    