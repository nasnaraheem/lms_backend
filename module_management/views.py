from django.shortcuts import render,get_object_or_404
from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions
from module_management.seralizers import ModuleSerializer
from course_management.models import Course
from module_management.models import Module

# Create your views here.

class ModuleCreateView(CreateAPIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ModuleSerializer

    def perform_create(self, serializer):

        course_id=self.kwargs.get("pk")
        course_object=get_object_or_404(Course,id=course_id)

      

        return serializer.save(course=course_object)

class ModuleRetriveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=ModuleSerializer
    queryset=Module.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


