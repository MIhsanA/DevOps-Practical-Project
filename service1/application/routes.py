from application import app, db, bcrypt
from flask import Flask, render_template, redirect, url_for, request
from application.forms import PersonForm
from application.models import Person
import requests
import random



@app.route('/', methods=['GET'])
def home():
    number = requests.get('http://service2:5001/number')
    id = number
    name= Person.query(Person.name).get(id)
    car = requests.get('http://service3:5002/car')
    dec= {'car':car.text, 'name':name}
    colour = requests.post('http://service4:5003/colour', data=dec)
    return render_template('home.html', person=person, number=number, car=car, colour=colour)
@app.route('/new', methods=['GET', 'POST'])
def new_person():
    form =PersonForm()
    if form.validate_on_submit():
        new_person = Persons(name=form.name.data)
        db.session.add(new_person)
        db.session.commit()
        return rdirect(url_for('home'))
    return render_template('new_persom.html', form=form)

