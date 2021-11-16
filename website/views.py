"""
created by : Hatim Zahid
Purpose : CRUD operations on a MongoDB database
Dated : 11/16/2021

"""

from flask import Blueprint, render_template , request
from flask.wrappers import Response
import pymongo
import json
from bson.objectid import ObjectId


# Connecting to the database server.
try:
    mongo = pymongo.MongoClient(
        host = "localhost" ,
         port = 27017,
         serverSelectionTimeoutMS = 1000
         )
    db = mongo.company
    mongo.server_info()
except:
    print("ERROR - Cannot connect ")


views = Blueprint('views', __name__)

# Home page is viewd on an HTML template
# html template is created in templates folder
@views.route('/')
def home():
    return render_template("home.html")


@views.route('/About')
def about():
    return "<p>Hatim Zahid</p>"


# READ the data from the database
@views.route('/All-Users')
def get_contactInfo():
    
    try:
        data = list (db.users.find())
        for user in data:
            user["_id"] = str( user["_id"]    )
        
        
        return str (data)

    except Exception as ex:
        print(ex)

        return Response(
            response = json.dumps({"message" : "cannot read users"    }) ,
            status= 200 ,
            mimetype= "application/json"
        )



#CREATE data in the database
@views.route('/sign-up' , methods = ['GET' , 'POST'])
def signup():
    if request.method == 'POST' :
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        try:
            user = {"name" : firstName , 
                    "email": email }
            dbresponse = db.users.insert_one(user)
            
        except Exception as ex:
            print (ex)
     
    return render_template("sign_up.html")
    

# CREATE USERS through POSTMAN (OPTIONAL)
@views.route( "/users"  , methods = ["POST"])
def create_user():
    try:
        user = {"name" : request.form["name"] , 
             "lastName": request.form["lastName"] }
        dbresponse = db.users.insert_one(user)
        print(dbresponse.inserted_id)
        return Response(
            response = json.dumps({"message" : "user-created"    }) ,
            status= 200 ,
            mimetype= "application/json"

        )
    except Exception as ex:
        print (ex)


#UPDATE USERS based on the ID which will be given in URL
@views.route( "/update/<id>"  , methods = ["PATCH"])
def update_user(id):
    try:
        queryAt = {"_id" : ObjectId(id)}
        updateWhat = {"$set" : {"name": request.form["name"] , "email": request.form["email"]}}
        dbresponse = db.users.update_one(queryAt , updateWhat)
        if dbresponse.modified_count == 1:
            return Response(
                response = json.dumps({"message" : "user-Updated"    }) ,
                status= 200 ,
                mimetype= "application/json")

        else:
             return Response(
                response = json.dumps({"message" : "Nothing to Update"    }) ,
                status= 200 ,
                mimetype= "application/json")

    except Exception as ex:
        print (ex)
        return Response(
            response = json.dumps({"message" : "user-not-updated"    }) ,
            status= 500 ,
            mimetype= "application/json"
        )


#DELETE USERS based on ID given through URL
@views.route( "/delete/<id>"  , methods = ["DELETE"])
def delete_user(id):
    try:
        queryAt = {"_id" : ObjectId(id)}
        dbresponse = db.users.delete_one(queryAt)
        #If the user didnt even existed it would always give response message,hence 
        #we can check here if delete operation was performed
        if dbresponse.deleted_count == 1:
            return Response(
                response = json.dumps({"message" : "user-Deleted"    }) ,
                status= 200 ,
                mimetype= "application/json")

        else:
             return Response(
                response = json.dumps({"message" : "Nothing to Update"    }) ,
                status= 200 ,
                mimetype= "application/json")

    except Exception as ex:
        print (ex)
        return Response(
            response = json.dumps({"message" : "user-not-deleted"    }) ,
            status= 500 ,
            mimetype= "application/json"
        )
