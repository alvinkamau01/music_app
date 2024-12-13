from utils.config import db
from marshmallow import Schema, fields

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.String, nullable=False)  # Use appropriate date type if needed
    banner_photo = db.Column(db.String, nullable=True)
    professionals_id=db.Column(db.String, db.ForeignKey('professionals.id'),nullable=True)

    professionals = db.relationship('Professional', back_populates='events')
    tickets = db.relationship('Ticket', back_populates='events')

    def __repr__(self):
        return f"<Event (id={self.id}, name={self.name}, date={self.date})>"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "description": self.description,
            "price": self.price,
            "date": self.date,
            "banner_photo": self.banner_photo,
        }

