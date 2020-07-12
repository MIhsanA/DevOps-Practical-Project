from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import random
import requests
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
@app.route('/number', methods=['GET'])
def number():
    person= Person.query.all()
    number = random.randint(1,len(person)-1)
    return Response(str(number), mimetype='text/plain')
if __name__ == '__main__':
    app.run(debug=True,port=5001, host='0.0.0.0')
