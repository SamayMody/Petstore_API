from fastapi import FastAPI
import db
import modals
app = FastAPI()


@app.get("/all")
def get_all():
    data = db.all()
    return {"data": data}


@app.post("/create")
def create(data:modals.Petstore):
    id = db.create(data)
    return {"inserted": True, "inserted_id": id}

@app.get("/get")
def get_one(pet_name:str):
    data = db.get_one(pet_name)
    return {"data":data}

@app.delete("/delete")
def delete(pet_name:str):
    data = db.delete(pet_name)
    return {"deleted": True , "deleted_count": data}

@app.put("/update")
def update(data:modals.Petstore):
    data = db.update(data)
    return {"updated": True, "updated_count": data}
