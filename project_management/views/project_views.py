import logging

from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from project_management.serializers.project_serializers import ProjectSerializer
from project_management.services.project_services import *

LOGGER = logging.getLogger(__name__)


# class MyIndex(APIView):
#     def get(self, request, project_name):
#         """
#         Dummy response for check
#         """
#         LOGGER.info("Rohit")
#         return HttpResponse("Hello.... You're at the Project index.")

class ProjectAPI(APIView):
    """
    API for CRUD operations of Project.
    Create/Read/Update/Delete
    """

    def get(self, request, project_name, format=None):
        """
        Request-type: GET
        Method for fetching Project details using 'project_name'
        """
        result = get_project(request, project_name)
        if result:
            response_serializer = ProjectSerializer(result)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No Data Found"}, status=status.HTTP_200_OK)

    def delete(self, request, project_name, format='json'):
        """
        Request-type: DELETE
        Method to remove a Project
        """
        result = delete_project(project_name)
        if result:
            return Response({"message": "Deleted Successfully."}, status=status.HTTP_200_OK)
        return Response({"message": "No Data Found."}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        """
        Request-type: POST
        Method for Creating Project
        """
        data = request.data
        request_serializer = ProjectSerializer(data=data)
        if request_serializer.is_valid():
            result = create_project(data)
            if result:
                response_serializer = ProjectSerializer(result)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            return Response({"message": "Operation failed."}, status=status.HTTP_417_EXPECTATION_FAILED)
        return Response({"message": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format='json'):
        """
        Request-type: PUT
        Method for Updating Project Details
        """
        data = request.data
        request_serializer = ProjectSerializer(data=data)
        if request_serializer.is_valid():
            result = update_project(data)
            if result:
                return Response({"message":"Updated Successfully."}, status=status.HTTP_200_OK)
            return Response({"message": "No Data Found."}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message":"Invalid Data."},status=status.HTTP_400_BAD_REQUEST)

class GetAllProjectsAPI(APIView):
    """
    API for getting All Project Details
    """

    def get(self, request, format=None):
        """
        Request-type: GET
        Method to fetch All Projects Details
        """
        result = get_all_projects()
        if result:
            response_serializer = ProjectSerializer(result, many=True)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No Data Found."}, status=status.HTTP_204_NO_CONTENT)
