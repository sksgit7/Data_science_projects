from app import app
from app.forms import InputForm
from flask import render_template,flash,redirect, url_for, request
import pickle
import numpy as np
import pandas as pd

def predict_price(area_type,location,sqft,bath,balcony,bhk):
    lr=pickle.load(open('bangalore_home_prices_model.pickle','rb'))
    a=pd.read_json('columns2.json')

    if location!='other':
    	loc_index=np.where(a.data_columns==location)[0][0]
    if area_type!='Carpet  Area':
    	area_index=np.where(a.data_columns==area_type)[0][0]
    
    x=np.zeros(len(a.data_columns))
    x[0]=float(sqft)
    x[1]=float(bath)
    x[2]=float(balcony)
    x[3]=float(bhk)
    if location!='other' and loc_index>=0:
        x[loc_index]=1
    if area_type!='Carpet  Area' and area_index>=0:
        x[area_index]=1
        
    return lr.predict([x])[0]

@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
def index():
    form=InputForm()
    if form.validate_on_submit():
    	print(form.area.data,form.loc.data,form.sqft.data,form.bath.data,form.balcony.data,type(form.bhk.data))
    	price=predict_price(form.area.data,form.loc.data,form.sqft.data,form.bath.data,form.balcony.data,form.bhk.data)
    	return render_template('login.html',price=round(price,2),form=form)
    return render_template('login.html', title='Input', form=form)