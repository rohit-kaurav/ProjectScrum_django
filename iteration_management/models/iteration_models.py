# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import DynamicDocument, fields

# Create your models here.
class Iteration(DynamicDocument):
    iteration_id = fields.StringField()
    project_id = fields.StringField()
    iteration_name = fields.StringField()
    description = fields.StringField()
    created = fields.StringField()
    date_modified = fields.StringField()
    completed = fields.StringField()
    status = fields.StringField()