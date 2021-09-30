from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime
import math
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Message:
    def __init__( self , data ):
        self.id = data['id']
        self.message = data['message']
        self.author_id = data['author_id']
        self.author = data['author']
        self.recipient_id = data['recipient_id']
        self.recipient = data['recipient']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    
    @classmethod
    def get_all_by_recipient(cls, data):
        query = "SELECT users.first_name as author, users2.first_name as recipient, messages.* FROM users LEFT JOIN messages ON users.id = messages.author_id LEFT JOIN users as users2 ON users2.id = messages.recipient_id WHERE users2.id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('user_messages').query_db(query, data)
        # Create an empty list to append our instances of friends
        messages = []
        # Iterate over the db results and create instances of friends with cls.
        for message in results:
            messages.append( cls(message) )
        return messages
    
    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at

        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hours ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"

    @classmethod
    def save(cls, data):
        query = "INSERT INTO messages ( message, author_id, recipient_id, created_at, updated_at) VALUES ( %(message)s, %(author_id)s, %(recipient_id)s, NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('user_messages').query_db( query, data )

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM messages WHERE id=%(id)s"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('user_messages').query_db( query, data )
