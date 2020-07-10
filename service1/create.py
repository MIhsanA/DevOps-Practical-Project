from application import db
from application.models import Person

db.drop_all()
db.create_all()
