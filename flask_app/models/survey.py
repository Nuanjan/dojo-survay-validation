# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask import flash


class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Now we use class methods to query our database

    @staticmethod
    def validate_survay(surveyFormData):
        is_valid = True  # we assume this is true
        if len(surveyFormData['name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if surveyFormData['location'] == "None":
            flash("You must select one location")
            is_valid = False
        if surveyFormData['language'] == "None":
            flash("You must select one language")
            is_valid = False
        if len(surveyFormData['comment']) < 5:
            flash("Please Comment at least 5 Character!")
            is_valid = False
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM surveys;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        # Create an empty list to append our instances of users
        surveys = []
        # Iterate over the db results and create instances of users with cls.
        for survey in results:
            surveys.append(cls(survey))
        return surveys

    @classmethod
    def add_survey(cls, data):
        query = "INSERT INTO surveys (name , location , language, comment , created_at, updated_at ) VALUES ( %(name)s , %(location)s , %(language)s, %(comment)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        # will return the id of that data that we just insert in
        return connectToMySQL('dojo_survey_schema').query_db(query, data)

    @classmethod
    def get_survey(cls, data):
        query = "SELECT * FROM surveys WHERE surveys.id = %(id)s;"
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        surveys = []
        for survey in results:
            surveys.append(cls(survey))
        return surveys[0]
