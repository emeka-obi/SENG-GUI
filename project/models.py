from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Coursedata(db.Model):
    __tablename__ = 'sweng_new_1'
    Code = db.Column(db.Integer)
    TAMUK = db.Column(db.Integer)
    Subject = db.Column(db.String(4))
    Course = db.Column(db.Integer)
    CRN = db.Column(db.Integer, primary_key = True)
    Section = db.Column(db.Integer)
    Credit = db.Column(db.Integer)
    LD_HC = db.Column(db.Integer)
    UD_HC = db.Column(db.Integer)
    MS_HC = db.Column(db.Integer)
    DRR_HC = db.Column(db.Integer)
    DRP_HC = db.Column(db.Integer)
    Year = db.Column(db.Integer)

    
    def __repr__(self) -> str:
        return "<Coursedata(Code={},TAMUK={}, Subject={},Course={}, CRN={}, Section={})".format(
            self.Code, self.TAMUK, self.Subject, self.Course, self.CRN, self.Section)