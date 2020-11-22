from app import db
from sqlalchemy.dialects.postgresql import JSON
class USERS(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    screen_name = db.Column(db.String())
    meta=db.Column(db.String())

    def __init__(self, screen_name, meta):
        self.screen_name=screen_name
        self.meta=meta


    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return 
        {
            'id': self.id, 
            'screen_name': self.screen_name,
            'meta': self.meta
        }