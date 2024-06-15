from pymongo import MongoClient

class MongoDBHandler:
    def __init__(self, uri="mongodb://localhost:27017/"):
        self.uri = uri
        self.client = None
        self.db = None
        self.collection = None
    
    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            print("Connected to MongoDB")
            return self.client
        except Exception as e:
            print(f"An error occurred while connecting to MongoDB: {e}")
    
    def close_connection(self):
        if self.client:
            self.client.close()
            print("Connection to MongoDB closed")



