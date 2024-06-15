from pymongo import MongoClient

def connect_to_mongodb(uri="mongodb://localhost:27017/"):
    client = None
    try:
        client = MongoClient(uri)
        print("Connected to MongoDB")
    except Exception as e:
        print(f"An error occurred while connecting to MongoDB: {e}")
    return client

def close_connection(client):
    if client:
        client.close()
        print("Connection to MongoDB closed")

# Example usage:
if __name__ == "__main__":
    mongo_client = connect_to_mongodb()
    db = mongo_client['newTest']
    collection = db['mycollection']
    print(collection.drop())
    # insert = collection.update_one({'age':'100'},{'$set':{'name':'poojith','age':'102'}})
    insert = collection.count_documents({'name':'poojith'})
    print(insert)
    # print(insert)
    # delete = collection.delete_many({'age':'104'})
    reords = collection.find({})
    for i in reords:
        print(i)

    # Use the client object to perform database operations...

    # Close the connection when done
    close_connection(mongo_client)
