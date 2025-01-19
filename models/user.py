
from utils.config import db  # Replace 'your_app' with the actual module name where db is defined

class User(db.Model):  # Inherit from db.Model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String, nullable=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    confirm_password = db.Column(db.String, nullable=False)  # Note: You typically wouldn't store this in the DB

    song_requests = db.relationship('SongRequest', back_populates='users')

    def __repr__(self):
        return f"<User  (id={self.id}, username={self.username}, email={self.email})>"
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'image': self.image,
            'password':self.password,
            'confirm_password':self.confirm_password

        }