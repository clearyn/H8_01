from datetime import datetime
from config import db, ma

class Avocado(db.Model):
    __tablename__ = 'avocado'
    # date = db.Column(db.Date, primary_key=True)
    # lname = db.Column(db.String(32), index=True)
    # fname = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Avocado
        sqla_session = db.session
        load_instance = True