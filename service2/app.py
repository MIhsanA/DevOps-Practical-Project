from flask import Flask, Response, Requests
from flask_sqlalchemy import SQLAlchemy
import random
import requests
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
@app.route('/number', methods=['GET'])
def number():
    #person= Person.query.all()
    number = random.randint(1,10)
    return Response(str(number), mimetype='text/plain')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
