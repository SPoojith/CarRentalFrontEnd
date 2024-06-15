
from flask import Flask, request
import json

import connections
# Add the directory containing `dbConnections` to the Python path
import sys
import os

# Add the parent directory containing `domain` to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.dbConnections import MongoDBHandler


app = Flask(__name__)



@app.route('/')
def renturadd():
    lists = []
    obj= {
        'a':{
            'b':[1,2,3]
        }
    }
    data = request.args.get('name')
    return str("hello  to your serer")

@app.route('/welcome',methods=['GET', 'POST'])
def hello_world():
    # data = {
    #     'a':'swift',
    #     'b':'santro'
    # }
    # Json = json.dumps(data)
    # return data
    return 'hi welcome to our server'


@app.route('/rides')
def model():
    return 'hi this is model'

@app.route('/list')
def add():
    # a = request.args.get('a')
    # b = request.args.get('b')
    mongo_handler = MongoDBHandler()
    mongo_client = mongo_handler.connect()
    db = mongo_client['newTest']
    collection = db['mycollection']
    reords = collection.find()
    # reords = collection.find({'age':{'$eq':30}})
    listr = ['hi']
    for i in reords:
        print(i)
        listr.append(i)
    return str(listr)

@app.route('/pop')
def pop():
    a = request.args.get('a')
    mongo_client = connections.connect_to_mongodb()
    db = mongo_client['newTest']
    collection = db['mycollection']
    reords = collection.delete_one({'age':a})
    # reords = collection.find({'age':{'$eq':30}})
    # listr = []
    # for i in reords:
    #     print(i)
    #     listr.append(i)
    return str(reords)


@app.route('/math')
def math():
    a = int(request.args.get('a'))
    print(type(a))
    b = int(request.args.get('b'))
    sum = a+b
    diff = a-b
    prod = a*b
    data = {
        'add' : sum,
        'diff':diff,
        'prod':prod
    }
    return json.dumps(data)



@app.route('/AddCars',methods=['GET','POST'])
def AddCars():
    mongo_handler = MongoDBHandler()
    mongo_client = mongo_handler.connect()
    db = mongo_client['CarRental']
    collection = db['OwnedCars']
    data = request.form['Data']  # pass the form field name as key
    Data = json.loads(data)
    model = Data.get('model')
    color = Data.get('color')
    rentCostPerKilometer = Data.get('rentCostPerKilometer')
    Number = Data.get('Number')
    Type = Data.get('type')
    try:
        reords = collection.insert_one({      
                'type':Type,
                'model' : model,
                'color' : color,
                'rentCostPerKilometer' : rentCostPerKilometer,
                'Number' : Number,
            })
        if reords.acknowledged != True:
            return str("Record Not Inserted, Try Again Later")

    except Exception as e:
        print(e)
        return str("Record Not Inserted, Try Again Later")
    
    return str("Record Inserted successfully")


@app.route('/getCarModel')
def getCarModel():
    mongo_handler = MongoDBHandler()
    mongo_client = mongo_handler.connect()
    db = mongo_client['CarRental']
    collection = db['OwnedCars']
    data = request.form['Data']  # pass the form field name as key
    Data = json.loads(data)
    model = Data.get('type')
    reords = collection.find({'type':model})
    # reords = collection.find({'age':{'$eq':30}})
    listr = []
    for i in reords:
        print(i)
        listr.append(i)
    return str(listr)


@app.route('/deleteOwndenCar')
def deleteOwndenCar():
    try:
        mongo_handler = MongoDBHandler()
        mongo_client = mongo_handler.connect()
        db = mongo_client['CarRental']
        collection = db['OwnedCars']
        model = request.args.get('model')
        reords = collection.delete_one({'model':model})
    except Exception as e:
        print(e)
        return str("Record Not removed, Try Again Later")
    return str("Record removed successfully")



@app.route('/updateOwndenCar')
def updateOwndenCar():
    try:
        mongo_handler = MongoDBHandler()
        mongo_client = mongo_handler.connect()
        db = mongo_client['CarRental']
        collection = db['OwnedCars']
        model = request.args.get('model')
        color = request.args.get('color')
        reords = collection.update_one({'model': model}, {'$set': {'color': color}})
        if reords.modified_count == 0:
            return str("Record Not update, Try Again Later. check for model name")
    except Exception as e:
        print(e)
        return str("Record Not update, Try Again Later")
    return str("Record update successfully")










# main driver function
if __name__ == '__main__':
    # print("hi")
    # run() method of Flask class runs the application 
    # on the local development server.
    # app.run()
    app.run(host='0.0.0.0', port=5656)


