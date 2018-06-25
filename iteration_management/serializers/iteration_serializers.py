from rest_framework_mongoengine.serializers import DynamicDocumentSerializer

from iteration_management.models.iteration_models import Iteration


class IterationSerializer(DynamicDocumentSerializer):
    class Meta(object):
        model = Iteration
        fields = ('iteration_id','project_id','iteration_name','description','created','date_modified','completed','status')


# class IterationResponseSerializer(DynamicDocumentSerializer):
#     class Meta(object):
#         model = iteration
#         fields = ('iteration_id','project_id','description','created','date_modified','completed','status')