# Petstore_API

/* Hello this is CAND7453
I have choosen to do Backend task 1 (i.e) creating a "Pet Store API" and was succesful in developing one within the stipulated time. Having no knowledge about any API's framework or databases i first learnt to create a basic CRUD operation usinf the fastapi framework. Then i learnt how to integreat it to MongoDB database as that is where all the data will be saved permanently and not like that in fastapi swagger ui where the data is stored temporaryly.*/

// Now i will give a short explanation on what each file function is!


/* db.py :
In this file we have written the program that connects us to the mongodb server.After establishing the connection we write the program to perform CRUD operations.So we declare collection as a dict and only in this all the data is gathered or collected.So as you can see " def.create(data): " is basically post (i.e) the user enters the data.Similarily " def all(): " is used to get all the data present in the collection. " def update(data) " is to Update the info and " def delete(name) " is where the data of the specific pet_name is removed from the collection. */

/* modals.py :
If we try posting anything then the swagger ui will demand for it in querry format which we don't want we only need  certain data from the user, so we create this file where a class is mentioned in which there are attributes such as pet_name , owner_name , age_of_pet , type and gender.

/*main.py : 
In this file we import the db.py and modals.py files.After that we create "get" , "post" , "delete" and "put" operations to perform the CRUD operations. So now when any user updates the data in localhost:8000/docs (i.e) FastAPI Swagger Ui , that data will be saved in our collection in MongoDb which is named as 'Petstore'.

//We connect the database through MongoDb compass as it is very simple through this method.
