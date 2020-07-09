from application import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    
    def __repr__(self):
        return ''.join([
            'PersonID: ', str(self.id), '\r\n',
            'Name: ', self.name
        ])

