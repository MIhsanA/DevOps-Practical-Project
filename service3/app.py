from flask import Flask, Response 
import requests
import random
app =Flask(__name__)

@app.route('/car', methods=['GET'])
def car():
    cars = ['bmw', 'volvo', 'tesla', 'jeep', 'honda', 'toyota', 'mazda', 'volkswagen', 'kia', 'mercedes']
    car = random.choice(cars)
    return Response(car, mimetype='text/plain')


if name == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)
