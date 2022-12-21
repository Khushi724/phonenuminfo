from flask import Flask, render_template
from flask import request
from time import time
from numpy import number
import phonenumbers
from phonenumbers import timezone, geocoder , carrier
app=Flask(__name__, static_url_path='/static')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/' , methods=['POST'])
def getval():
    number=request.form['nu']
    phone= phonenumbers.parse(number)
    time=timezone.time_zones_for_number(phone)
    car=carrier.name_for_number(phone, "en")
    reg=geocoder.description_for_number(phone,"en")
    return render_template('st.html',time=time, car=car, reg=reg, phone=phone)
app.run(host="0.0.0.0" ,port=90)

