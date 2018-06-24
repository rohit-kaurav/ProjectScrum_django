import logging

from project_management.models.project_models import Project
import datetime
import json

LOGGER = logging.getLogger(__name__)


def get_project(request, project_id):
    """
    Get a Project detail.
    """
    try:
        obj = Project.objects.get(project_id=project_id)
    except(Exception):
        print (Exception.message)
    else:
        return obj
    return None

def get_all_projects():
    """
    Get Details of all Projects here.
    """
    try:
        obj = Project.objects.all()
    except(Exception):
        print (Exception.message)
    else:
        return obj


def create_project(input_dict):
    """
    Add a New Project to the database here.
    """
    try:
        project_obj = Project(input_dict.get('project_id'),input_dict.get('employee_id'),input_dict.get('project_name'),input_dict.get('description'),input_dict.get('created'),input_dict.get('date_modified'),input_dict.get('status')).save()
    except(Exception):
        print (Exception)
    else:
        return project_obj
    return None

def update_project(input_dict):
    """
    Editing and updating required fields of project.
    """
    try:
        project_obj = Project.objects(project_id=input_dict.get('project_id')).update(project_name=input_dict.get('project_name'))
    except(Exception):
        print (Exception)
    else:
        return project_obj
    return None

def delete_project(project_id):
    """
    Deleting a Project from database here.
    """
    try:
        project_obj = Project.objects(project_id=project_id).delete()
    except(Exception):
        print (Exception)
    else:
        return project_obj
    return None
