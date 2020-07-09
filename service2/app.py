from flask import Flask, Response, request
import random
import requests
app = Flask(__name__)


@app.route('/number', methods=['GET'])
def number():
    number = random.randint(1,10)
    return Response(str(number), mimetype='text/plain')


    


if __name__ == '__main__':
    app.run(debug=True,port=5001, host='0.0.0.0')
