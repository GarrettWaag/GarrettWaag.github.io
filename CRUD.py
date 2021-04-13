from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import pymongo

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, db):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        adress = 'mongodb://%s:%s@localhost:27017/'+str(db)
        self.client = MongoClient(adress  % (username, password))
        self.database = self.client['AAC']
        

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                entry = self.database.animals.insert_one(data)  # data should be dictionary  
                print("Sucessful insert")
            except pymongo.errors.PyMongoError as errorCode:
                print(str(errorCode))
            
               
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, key):
        if key is not None:
            try:
                results = list(self.database.animals.find(key,{"_id":False})) #returns cursor as list
                return results
            except pymongo.errors.PyMongoError as errorCode:
                print(str(errorCode))
            
        else:
            raise Exception("Nothing found")
            
            
    def update(self, target, data):
        if target and data is not None:
            record = self.read(target)
            for r in record:
                try:
                    result = self.database.animals.update_one(target, {"$set": data})
                    if result.acknowledged:
                        json_data = json.dumps(self.database.animals.find(data), default=str)
                        print(json_data)
                except pymongo.errors.PyMongoError as errorCode:
                    print(str(errorCode))
        else:
            raise Exception("Nothing found")
   
    def delete(self, target):
        if target is not None:
            record = self.read(target)
            for r in record:
                try:
                    result = self.database.animals.delete_one(target)
                    if result.acknowledged:
                        json_data = json.dumps(result, default=str)
                        print(json_data)
                except pymongo.errors.PyMongoError as errorCode:
                    print(str(errorCode))
     