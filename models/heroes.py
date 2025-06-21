from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from models.hero_power import Hero_Power
from models.conn import db


class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)

    # recursions
    serialize_rules = ('-hero_powers.hero',)

    # proxies
    powers = association_proxy('hero_powers', 'power',
                               creator=lambda power_obj: Hero_Power(power=power_obj))
    
    # relationship
    hero_powers = db.relationship("Hero_Power", back_populates = "hero")

    def __repr__(self):
        return f'<Heroes {self.id}, {self.name}, {self.super_name}>'
