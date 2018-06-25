import logging

from project_management.models.project_models import Project
from datetime import datetime
import uuid
import json

LOGGER = logging.getLogger(__name__)


def get_project(request, project_name):
    """
    Get a Project detail.
    """
    try:
        obj = Project.objects.get(project_name=project_name)
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
    now = datetime.now().isoformat()
    project_id = str(uuid.uuid1())
    try:
        project_obj = Project(project_id,input_dict.get('employee_id'),input_dict.get('project_name'),input_dict.get('description'),now,now,"New").save()
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
        project_obj = Project.objects(project_id=input_dict.get('project_id')).update(project_name=input_dict.get('project_name'),status="In Progress")
    except(Exception):
        print (Exception)
    else:
        return project_obj
    return None

def delete_project(project_name):
    """
    Deleting a Project from database here.
    """
    try:
        project_obj = Project.objects(project_name=project_name).delete()
    except(Exception):
        print (Exception)
    else:
        return project_obj
    return None
