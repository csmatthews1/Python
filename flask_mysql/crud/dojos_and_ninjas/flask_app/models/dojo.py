# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            data = {
                "id": row["ninjas.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "created_at": row["ninjas.created_at"],
                "updated_at": row["ninjas.updated_at"]
            }
            dojo.ninjas.append( Ninja(data))
        return dojo

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name, created_at, updated_at) VALUES ( %(name)s, NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )

    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)