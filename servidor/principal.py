from flask import Flask, jsonify, request

app=Flask(__name__)

feedbacks=[
	{ 
	"title": "Experienced salespeople",
	"name": "Alex H.",
	"date": "2020-02-02",
	"feedback": "It was great to talk to the salespeople in the team"
	}
]

@app.route("/hello")
def hello_world():
	return "Hello, World!"

@app.route("/")
def get_feedbacks():
	return jsonify(feedbacks)
