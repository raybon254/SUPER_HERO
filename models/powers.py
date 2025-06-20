
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from models.hero_power import Hero_Power
from models.conn import db

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

     # recursions
    serialize_rules = ('-hero_powers.power')

     # proxies
    heroes = association_proxy('heroes_powers', 'hero',
                               creator=lambda power_obj: Hero_Power(power=power_obj))
    
    # relationship
    hero_powers = db.relationship("Hero_Power", back_populates = "power")

    def __repr__(self):
        return f'<Powers {self.id}, {self.name}, {self.description}>'
