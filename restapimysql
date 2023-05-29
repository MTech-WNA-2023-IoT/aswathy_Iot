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

#assign Flask-Mysql Module
sql=MySQL()

#Configure MySQL
app.config['MYSQL_DATABASE_USER'] = 'your-mysql-username'
app.config['MYSQL_DATABASE_PASSWORD'] = 'your-mysql-password'
app.config['MYSQL_DATABASE_DB'] = 'your-mysql-database'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

#initialise MySQL (connect to mysql)
mysql.init_app(app)

#Create 1st API function for testing
#once you open "localhost:<port>/" this function is executed.
#this is not mandatory but will help in testing the program

@app.route('/')
#Give a funtion name
def welcome():
#return is the data given by the API
	return "\tWelcome.... \tKindly use one of the APIs to get data"

#Create your first real API- "recentlocation" is the API that gives recent device location
#This API will fetch data from the MySQL Database and display it on the URL

@app.route('/API1')
def recentlocation():
#Create a MySQL Cursor	
	cur = mysql.connect().cursor()
#Execute the SQL
	cur.execute('select * from <your table> ORDER BY id DESC LIMIT 5 ')
#Receive the SQL Response in a variable
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
#Return the respose to the URL
	return jsonify({'Data' : r})

#Start the Flask program
if __name__ == '__main__':
#app.run will make the APIs available on this particular IP address and Port 5000
#0.0.0.0  ip means any one can access.
    app.run(host="0.0.0.0",debug=1)
