# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from user_management.serializers.user_serializers import UserRequestSerializer, UserResponseSerializer
from user_management.services.user_services import *
import uuid


class User(APIView):

    def get(self, request, employee_id, format=None):
        '''
        Returns user
        ---
        request_serializer = UserRequestSerializer
        response_serializer = UserResponseSerializer
        '''
        result = get_user(request, employee_id)
        if result:
            response_serializer = UserResponseSerializer(result)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response("Failed to fetch data", status=status.HTTP_406_NOT_ACCEPTABLE)

    def post(self, request, format=None):
        '''
        Add user
         ---
        request_serializer = UserRequestSerializer
        response_serializer = UserResponseSerializer
        '''
        user_data = request.data
        request_service = UserRequestSerializer(data=user_data)
        if request_service.is_valid():
            result = add_user(request, user_data)
            response_serializer = UserResponseSerializer(result)
            return Response(response_serializer.data, status.HTTP_200_OK)
        return Response("Not able to add user", status.HTTP_406_NOT_ACCEPTABLE)

    def put(self, request, format=None):
        '''
        Update user
        ---
        request_serializer = UserRequestSerializer
        response_serializer = UserResponseSerializer
        '''
        user_data = request.data
        request_service = UserRequestSerializer(data=user_data)
        if request_service.is_valid:
            result = add_user(request, user_data)
            return Response("Succesfully updated data", status.HTTP_200_OK)
        return Response("Updation failed", status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, employee_id, format=None):
        '''
        Delete user
        '''

        result = delete_user(employee_id)
        if result:
            return Response("Deletion Success", status.HTTP_200_OK)
        return Response("Deletion failed", status.HTTP_400_BAD_REQUEST)


class GetAllUser(APIView):

    def get(self, request, format=None):
        '''
        Returns all user
        ---
        request_serializer = UserRequestSerializer
        response_serializer = UserResponseSerializer
        '''

        result = get_all_user()
        if result:
            response_serializer = UserResponseSerializer(result, many=True)

            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response("Failed to fetch users data", status=status.HTTP_406_NOT_ACCEPTABLE)


class VerifyUser(APIView):

    def get(self, request, username, format=None):
        ''' Returns user by matching username
        '''

        user = get_user_by_username(request, username)
        if user:
            response_serializer = UserResponseSerializer(user)
            return Response({"message": "Found"}, status.HTTP_200_OK)
        return Response({"message": "Not Found"}, status.HTTP_200_OK)


class AuthorizeUser(APIView):

    def post(self, request, format=None):
        """
        Request-type: POST
        Method to authorize User with Username and Password
        """
        result = authorize_user(request.data)
        if result:
            response_serializer = UserResponseSerializer(result)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response({"invalid": True}, status=status.HTTP_400_BAD_REQUEST)
