
import uuid
from user_management.models.user import User
''' Services available for users are :
    1. add new user 
    2. update user details
    3. get user details
    4. delete user
    5. get all user details
'''

def get_user(request,employee_id):
    ''' Get user detail for employee using employee_id 
    '''
    try :
        user = User.objects.get(employee_id = employee_id)
    except(Exception):
        print(Exception)
    else:
        return user


def add_user(request,input_data):
    '''Add new user
    '''
    if request.method == "POST":
        result = get_all_user()
        role = ""
        if result:
            role = "employee"
        else:
            role = "manager"
        user_uid = str(uuid.uuid1())
        try:
            user_obj = User(input_data.get('name'),
                            input_data.get('employee_id'),
                            user_uid,
                            role,
                            input_data.get('username'),
                            input_data.get('password')).save()
        except(Exception):
            print(Exception.message)
        else :
            return user_obj
    else :
        try :
            is_user_updated = User.objects(employee_id = input_data.get('employee_id')).update(
                name = input_data.get('name'),role = input_data.get('role'), 
                username = input_data.get('username'), password = input_data.get('password'))
        except(Exception):
            print(Exception.message)
        else :
            return is_user_updated


def delete_user(employee_id):
    '''Delete user
    '''
    try :
        user_obj = User.objects(employee_id = employee_id)
        result = user_obj.delete()
    except(Exception):
        print(Exception.message)
    else:
        return result


def get_all_user():
    ''' Get all user details
    '''
    try:
        users_list = User.objects.all()
    except(Exception):
        print(Exception.message)
    else:
        return users_list

def get_user_by_username(request,username):
    ''' Get user detail for employee using employee_id 
    '''
    try :
        user = User.objects.get(username = username)
    except(Exception):
        print(Exception)
    else:
        return user

def authorize_user(credentials):
    """
    Verify User and return User data.
    """
    try:
        user = User.objects.get(username=credentials.get('username'),password=credentials.get('password'))
    except(Exception):
        print(Exception)
    else:
        return user