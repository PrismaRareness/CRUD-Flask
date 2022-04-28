from app import app


@app.route("/ola")
def ola():
    return "Olá, mundo em Flask"
