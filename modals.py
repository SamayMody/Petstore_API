from pydantic import BaseModel
class Petstore(BaseModel):
    pet_name: str
    owner_name: str
    age_of_pet: int
    type: str
    gender: str


