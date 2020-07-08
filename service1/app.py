from flask import Flask, render_template
import requests
import random
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
  listofperson=['robet', 'ben', 'ihsan', 'james', 'osin', 'bilal']
  person = random.choice(listofperson)

  number = requests.get('http://service2:5001/number')
  car = requests.get('http://service3:5002/car')
  colour = requests.post('http://service4:5003/colour' data=person.text, data2=car.text)
  return render_template('home.html', person=person, number=number, car=car, colour=colour)




if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
