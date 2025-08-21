from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)
load_dotenv()

client = MongoClient(os.getenv("MONGO_URL"))
db = client.mongo_database
collection = db.form_data
todo_collection = db.todo_items

@app.route('/')
def home():
    return "Greetings from the BACKEND"

@app.route('/submit', methods=['POST'])
def submit():
    try:
        form_data = dict(request.form)
        collection.insert_one(form_data)
        return "Data Submitted Successfully!"
    except:
        return "Error saving data"

@app.route('/add_todo', methods=['POST'])
def add_todo():
    try:
        todo_data = dict(request.form)
        todo_collection.insert_one(todo_data)
        return "To-Do Item Added Successfully!"
    except:
        return "Error saving to-do item"

@app.route('/api')
def get_data():
    return jsonify(list(collection.find({}, {'_id': 0})))

if __name__ == '__main__':
    app.run(port=3000, host='0.0.0.0', debug=True)
