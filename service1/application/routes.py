from application import app, db, bcrypt
from flask import Flask, render_template, redirect, url_for, request
from application.forms import PersonForm
from application.models import Person
import requests
import random



@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/genrate')
def generate():
    number = requests.get('http://service2:5001/number')
    id = int(number.text)
    name= Person.query.filter_by(id=id).first()
    new_name= str(name.name)
    car = requests.get('http://service3:5002/car')
    colour = requests.post('http://service4:5003/colour', new_name)
    return render_template('home.html', number=number, name=name.name, car=car, colour=colour)
@app.route('/new', methods=['GET', 'POST'])
def new_person():
    form =PersonForm()
    if form.validate_on_submit():
        new_person = Person(name=form.name.data)
        db.session.add(new_person)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('new_person.html', form=form)

