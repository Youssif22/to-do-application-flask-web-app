from todoapp import db, app
from datetime import datetime


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False)
    complete = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return "Todo('{}', {})".format(self.content, self.completed)

