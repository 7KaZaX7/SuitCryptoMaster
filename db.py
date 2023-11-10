from flask_sqlalchemy import SQLAlchemy
from run import app
from datetime import datetime

db = SQLAlchemy(app)


class Atricle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id
