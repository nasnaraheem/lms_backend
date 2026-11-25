from django.shortcuts import render,get_object_or_404
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from course_management.serializers import CourseSerializer
from rest_framework import authentication,permissions
from course_management.models import Course
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.permission import IsOwner

# Create your views here.
class CourseListCreateView(ListAPIView,CreateAPIView):

    
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=CourseSerializer

    def get_queryset(self):
        return Course.objects.filter(trainer=self.request.user)


    def perform_create(self, serializer):
        serializer.save(trainer=self.request.user)
    

    
    
class CourseRetriveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]

    queryset=Course.objects.all()
    serializer_class=CourseSerializer

   

    
        

