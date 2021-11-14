from config import db, ma
from marshmallow import fields
from sqlalchemy.orm import backref

#https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
#Many To One Avoregion
#Many To One Avotype
class Avocado(db.Model):
    __tablename__ = 'avocado'
    __table_args__ = (
        db.PrimaryKeyConstraint('avgprice', 'totalvol', 'date'),
    )
    date = db.Column(db.String(60))
    avgprice = db.Column(db.Float)
    totalvol = db.Column(db.Integer)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Float)
    avo_c = db.Column(db.Float)
    type = db.Column(db.Integer, db.ForeignKey('avotype.typeid'))
    regionid = db.Column(db.Integer, db.ForeignKey('avoregion.regionid'))
    p_avotype = db.relationship("Avotype")
    p_avoregion = db.relationship("Avoregion", backref=backref("avocado"))

class Avoregion(db.Model):
    __tablename__ = 'avoregion'
    regionid = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(60))

class Avotype(db.Model):
    __tablename__ = 'avotype'
    typeid = db.Column(db.Integer, primary_key=True)
    typ = db.Column(db.String(60))
    

#https://flask-marshmallow.readthedocs.io/en/latest/
# Marsmallow relationship
class AvocadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Avocado
        include_fk = True
        load_instance = True

    type = ma.auto_field()
    regionid = fields.Nested("TAvoregionSchema", default=None)

class AvoregionSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Avoregion
        include_relationships = True
        load_instance = True

    avocado = fields.Nested('TAvocadoSchema', default=[], many=True)

class AvotypeSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Avotype
        include_relationships = True
        load_instance = True

    avocado = fields.Nested('TAvocadoSchema', default=[], many=True)

class TAvocadoSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    date = fields.Str()
    avgprice = fields.Float()
    totalvol = fields.Int()
    avo_a = fields.Int()
    avo_b = fields.Float()
    avo_c = fields.Float()
    type = fields.Int()
    regionid = fields.Int()

class TAvoregionSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    regionid = fields.Int()
    region = fields.Str()

class TAvotypeSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    typeid = fields.Int()
    type = fields.Str()