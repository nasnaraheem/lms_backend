from rest_framework import serializers
from course_management.models import Course
from module_management.models import Module
from module_management.seralizers import ModuleSerializer

class CourseSerializer(serializers.ModelSerializer):

    module_count=serializers.SerializerMethodField(read_only=True)
    module=serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=Course
        fields="__all__"
        read_only_fields=["id","trainer","slug","created_at","updated_at"]

    def get_module_count(self,obj):
        return Module.objects.filter(course=obj).count()

    def get_module(self,obj):

        qs=Module.objects.filter(course=obj)
        serializer_instance=ModuleSerializer(qs,many=True)
        return serializer_instance.data