import os
from flask import Flask, url_for, render_template, request, jsonify , redirect
from flask import *

app = Flask(__name__)

from clarifai.rest import ClarifaiApp

myApi='937179c1c41f4378b15017c3bc501ce4'
CLapp = ClarifaiApp(api_key=myApi)
model = CLapp.public_models.general_model

from tags import predict


@app.route('/')  
def home():
    return render_template('index.html')

@app.route('/results')
def results():
    imageLink = request.args['inputname']   

    results = predict(imageLink,myApi) 
    
    return render_template('results.html',concept0=results[0],concept1=results[1],concept2=results[2],concept3=results[3],concept4=results[4],concept5=results[5],concept6=results[6])

if __name__ == "__main__":
    app.run(debug=True)