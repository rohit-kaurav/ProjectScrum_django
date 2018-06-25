import logging

from iteration_management.models.iteration_models import Iteration
from datetime import datetime
import uuid
import json

LOGGER = logging.getLogger(__name__)


def get_iteration(request, iteration_name):
    """
    Get a Iteration detail.
    """
    try:
        obj = Iteration.objects.get(iteration_name=iteration_name)
    except(Exception):
        print (Exception.message)
    else:
        return obj
    return None

def get_all_iterations():
    """
    Get Details of all iterations here.
    """
    try:
        obj = Iteration.objects.all()
    except(Exception):
        print (Exception.message)
    else:
        return obj


def create_iteration(input_dict):
    """
    Add a New iteration to the database here.
    """
    now = datetime.now().isoformat()
    iteration_id = str(uuid.uuid1())
    try:
        iteration_obj = Iteration(iteration_id,input_dict.get('project_id'),input_dict.get('iteration_name'),input_dict.get('description'),now,now,None,"New").save()
    except(Exception):
        print (Exception)
    else:
        return iteration_obj
    return None

def update_iteration(input_dict):
    """
    Editing and updating required fields of iteration.
    """
    try:
        iteration_obj = Iteration.objects(iteration_id=input_dict.get('iteration_id')).update(iteration_name=input_dict.get('iteration_name'),description=input_dict.get('description'),status="In Progress")
    except(Exception):
        print (Exception)
    else:
        return iteration_obj
    return None

def delete_iteration(iteration_name):
    """
    Deleting a Iteration from database here.
    """
    try:
        iteration_obj = Iteration.objects(iteration_name=iteration_name).delete()
    except(Exception):
        print (Exception)
    else:
        return iteration_obj
    return None
