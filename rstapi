#!/usr/bin/python
#(c)Sai Shibu
#201904170935ISTV1
#Sample program for Rest APIs
#Install Required Packages
#	1)Flask (pip install Flask)
#	2)Flask-ext MySQL (pip install Flask-MySQL)
#	3)Flask - Jsonify(mostly included with Flask)

#import necessary modules
from flask import Flask, jsonify,request
from flaskext.mysql import MySQL

#assign a Flask Class
app=Flask(__name__)

@app.route('/')

#Give a funtion name
def welcome():

#return is the data given by the API
	return "\tWelcome.... \tKindly use one of the APIs to get data"

#Start the Flask program
if __name__ == '__main__':
#app.run will make the APIs available on this particular IP address and Port 5000
#0.0.0.0  ip means any one can access.
    app.run(host="0.0.0.0",debug=1)
