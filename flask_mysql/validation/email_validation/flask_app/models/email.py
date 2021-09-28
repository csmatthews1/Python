from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('emails').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_last(cls):
        query = "SELECT * FROM emails ORDER BY id DESC LIMIT 1;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        result = connectToMySQL('emails').query_db(query)
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails ( email, created_at, updated_at) VALUES ( %(email)s, NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('emails').query_db( query, data )

    @staticmethod
    def validate_email(email):
        is_valid = True;
        if not EMAIL_REGEX.match(email['email']): 
            flash("Email is not valid!")
            is_valid = False
        return is_valid
        return is_valid