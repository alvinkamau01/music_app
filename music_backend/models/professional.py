from utils.config import db

class Professional(db.Model):
    __tablename__ = 'professionals'

    id = db.Column(db.Integer, primary_key=True)
    song_path = db.Column(db.String, nullable=False)
    about = db.Column(db.Text, nullable=True)
    socials = db.Column(db.Text, nullable=True)  # JSON or string representation of social links
    banner_image = db.Column(db.String, nullable=True)

    events = db.relationship('Event', back_populates='professionals')

    def __repr__(self):
        return f"<Professional (id={self.id}, about={self.about})>"