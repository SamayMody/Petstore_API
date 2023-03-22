import pymongo
mongoURI = "mongodb://localhost:27017"

client = pymongo.MongoClient(mongoURI)
db = client["Petstore"]

collection = db["pets"]

def create(data):
    data = dict(data)
    response = collection.insert_one(data)
    return str(response.inserted_id)

def all():
    response = collection.find({})
    data=[]
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)
    return data

def get_one(condition):
    response = collection.find_one({"pet_name": condition})
    if response is not None:
        response["_id"] = str(response["_id"])
    return response


def update(data):
    data = dict(data)
    response = collection.update_one(
        {"pet_name": data["pet_name"]},
        {"$set": {
            "owner_name": data["owner_name"],
            "age_of_pet": data["age_of_pet"],
            "type": data["type"],
            "gender": data["gender"]
        }}
    )
    return response.modified_count


def delete(name):
    response = collection.delete_one({"pet_name": name})
    return response.deleted_count







