from datetime import datetime

from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return "<Todo: %s[%s]>" % (self.title, "DONE" if self.completed else "UNDONE")
