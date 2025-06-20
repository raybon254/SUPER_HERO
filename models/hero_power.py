
from models.conn import db
from sqlalchemy_serializer import SerializerMixin

class Hero_Power(db.Model,SerializerMixin ):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    
    # foreign
    hero_id = db.Column(db.Integer, db.ForeignKey("heroes.id"))
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"))

    # relationships
    hero = db.relationship("Hero", back_populates = "hero_powers")
    power = db.relationship("Power", back_populates = "hero_powers")

    # recursions
    serialize_rules = ('-hero.hero_powers', '-power.hero_powers',)

    def __repr__(self):
        return f'<Heroes {self.id}, {self.name}, {self.strength}>'
