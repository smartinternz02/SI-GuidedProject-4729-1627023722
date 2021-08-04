import os
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing  import image
import tensorflow as tf
from flask import Flask , request, render_template
from gevent.pywsgi import WSGIServer

app=Flask(_name_)

@app.route('/', methods=['GET'])
def Home():
    return render_template("Home.html")

@app.route('/predict')
def GetStarted():
    return render_template('Predict.html')
@app.route('/')
def index():
    return render_template('Predict.html')

@app.route('/predict',methods=['POST'])		
def predict():
    model_name=""
    excel_name=""
    plant=request.form['plant']
    if(plant=="vegetable"):
        model_name=r"E:\VIT\PlantFertilizerRecommendation\Flaskweb\vegetable.h5"
        excel_name='precautions - vegetables.xlsx'
    elif(plant=="fruit"):
        model_name=r"E:\VIT\PlantFertilizerRecommendation\Flaskweb\fruitnames.h5"
        excel_name='precautions - fruits.xlsx'
    a = request.files['image']
    basepath = os.path.dirname(_file_)
    filepath = os.path.join(basepath,'uploads',a.filename)
    a.save(filepath)
    img = image.load_img(filepath,target_size = (64,64))
    model = load_model (model_name)
    x = image.img_to_array(img)
    x = np.expand_dims(x,axis = 0)
    p=model.predict(x)
    pred = np.argmax(model.predict(x))
    df=pd.read_excel(excel_name)
    return render_template("Predict.html", result=df.iloc[pred.item(),0])
    
@app.route('/Logout')
def Logout():
    return render_template('Logout.html')

if _name_ ==  "_main_":
     app.run(debug=True)
