from mongoengine import DynamicDocument, fields
import json


class Project(DynamicDocument):
    project_id = fields.StringField()
    employee_id = fields.StringField()
    project_name = fields.StringField()
    description = fields.StringField()
    created = fields.StringField()
    date_modified = fields.StringField()
    status = fields.StringField()

    def __str__(self):
        # return ProjectResponseSerializer(self)
        return self.project_name
