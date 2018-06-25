# -*- coding: utf-8 -*-
from mongoengine import DynamicDocument, fields

class User (DynamicDocument) :
    
    ''' User model with following attributes
        name = String
        employee_id = String
        user_uid = String
        role = String
        credentials = {
            username : String
            password : String
        }
    '''
    name = fields.StringField()
    employee_id = fields.StringField()
    user_uid = fields.StringField()
    role = fields.StringField()
    username = fields.StringField()
    password = fields.StringField()
