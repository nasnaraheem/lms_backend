from rest_framework import serializers
from course_management.models import Course
from module_management.models import Module
from module_management.seralizers import ModuleSerializer
from lesson_management.models import Lesson
from django.db.models import Sum

class CourseSerializer(serializers.ModelSerializer):

    module_count=serializers.SerializerMethodField(read_only=True)
    module=serializers.SerializerMethodField(read_only=True)

    total_duration=serializers.SerializerMethodField(read_only=True)

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

    def get_total_duration(self,obj):
        return Lesson.objects.filter(module__course=obj).values("duration").aggregate(total=Sum("duration")).get("total",0)