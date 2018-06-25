import logging

from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from iteration_management.serializers.iteration_serializers import IterationSerializer
from iteration_management.services.iteration_services import *

LOGGER = logging.getLogger(__name__)

class IterationAPI(APIView):
    """
    API for CRUD operations of Iteration.
    Create/Read/Update/Delete
    """

    def get(self, request, iteration_name, format=None):
        """
        Request-type: GET
        Method for fetching iteration details using 'iteration_name'
        """
        result = get_iteration(request, iteration_name)
        if result:
            response_serializer = IterationSerializer(result)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No Data Found"}, status=status.HTTP_200_OK)

    def delete(self, request, iteration_name, format='json'):
        """
        Request-type: DELETE
        Method to remove an Iteration
        """
        result = delete_iteration(iteration_name)
        print ("what deleting ",result)
        if result:
            return Response({"message": "Deleted Successfully."}, status=status.HTTP_200_OK)
        return Response({"message": "No Data Found."}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        """
        Request-type: POST
        Method for Creating an Iteration
        """
        data = request.data
        request_serializer = IterationSerializer(data=data)
        if request_serializer.is_valid():
            result = create_iteration(data)
            if result:
                response_serializer = IterationSerializer(result)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            return Response({"message": "Operation failed."}, status=status.HTTP_417_EXPECTATION_FAILED)
        return Response({"message": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format='json'):
        """
        Request-type: PUT
        Method for Updating an Iteration Details
        """
        data = request.data
        request_serializer = IterationSerializer(data=data)
        if request_serializer.is_valid():
            result = update_iteration(data)
            if result:
                return Response({"message":"Updated Successfully."}, status=status.HTTP_200_OK)
            return Response({"message": "No Data Found."}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message":"Invalid Data."},status=status.HTTP_400_BAD_REQUEST)

class GetAllIterationsAPI(APIView):
    """
    API for getting All Iterations Details
    """

    def get(self, request, format=None):
        """
        Request-type: GET
        Method to fetch All Iterations Details
        """
        result = get_all_iterations()
        if result:
            response_serializer = IterationSerializer(result, many=True)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No Data Found."}, status=status.HTTP_204_NO_CONTENT)
