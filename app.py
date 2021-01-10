
import sys
sys.path.insert(0, "./modules")


from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
   return "Hello Flask"

@app.route("/users")
def users():
   users = [{'name': 'test1'}, {'name': 'test2'}]
   return jsonify(data=users)

@app.route("/users/<id>")
def user(id):
   return jsonify(data={'name': 'test1'})

@app.route("/gen_drum_groove", methods=['POST'])
def gen_drum_groove():
	req = request.get_json()
	tap_sounds = req.get('tap_sounds')
	# TODO: generate drum groove here
	return 'generated drum groove here ' + tap_sounds


