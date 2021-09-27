from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojo_survey').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_last(cls):
        query = "SELECT * FROM dojos ORDER BY id DESC LIMIT 1;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        result = connectToMySQL('dojo_survey').query_db(query)
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name, location, language, comment, created_at, updated_at) VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojo_survey').query_db( query, data )

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True;
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['comment']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid