from rest_framework_mongoengine.serializers import DynamicDocumentSerializer

from project_management.models.project_models import Project


class ProjectSerializer(DynamicDocumentSerializer):
    class Meta(object):
        model = Project
        fields = ('project_id','employee_id','project_name','description','created','date_modified','status')


# class ProjectResponseSerializer(DynamicDocumentSerializer):
#     class Meta(object):
#         model = Project
#         fields = ('project_id','employee_id','project_name','description','created','date_modified','status')