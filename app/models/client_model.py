from app import db
from sqlalchemy_utils import ChoiceType


class Client(db.Model):
    __tablename__ = 'clients'
    
    GENDER_CHOICES = [
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
        (u'N', u'Nenhuma das opções'),
    ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(200))
    birth_date = db.Column(db.DateTime)
    occupation = db.Column(db.String(30))
    gender = db.Column(ChoiceType(GENDER_CHOICES))
