from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, StringField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email


class ClientForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = EmailField("email", validators=[Email(), DataRequired()])
    birth_date = DateField("birth_date", validators=[DataRequired()], format='%d/%m/%Y')
    ocuppation = StringField("ocuppation", validators=[DataRequired()])
    gender = SelectField("gender", validators=[DataRequired()], choices=[('F', 'Feminino'), ('M', "Masculino"),
                                                                         ('N', 'Nenhuma das opções')])
