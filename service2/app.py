from flask import Flask, Response, 
import random
import requests

app = Flask(__name__)


@app.route('/number', methods=['GET'])
def number():
    number = random.randint(1,10)
    return Response(number, mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
