from flask import Flask,request,render_template
from datetime import datetime
app=Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = MONGO_URI

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db=client.test

collection=db['flask-tutorial']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    



@app.route('/')
def home():
    day_of_week=datetime.today().strftime('%A')
    print(day_of_week)
    current_time=datetime.now().strftime('%H:%M:%S')
    return render_template('index.html',day_of_week= day_of_week, current_time=current_time)

@app.route('/submit',methods=['POST'])
def submit():
    form_data=dict(request.form)
    collection.insert_one(form_data)
    return "Data submitted successfully."
    
@app.route('/view')
def view():
    data=collection.find()
    
    data=list(data)
    for item in data:
        print(item)
        del item['_id']  
    
    data = {
        'data':data
    }
    
    return data
        
        
if __name__ == "__main__":
    app.run(debug=True)