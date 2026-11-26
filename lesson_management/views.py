from django.shortcuts import render,get_object_or_404
from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import permissions,authentication
from lesson_management.serializers import LessonSerializer
from module_management.models import Module
from lesson_management.models import Lesson

# Create your views here.
class LessonCreateView(CreateAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=LessonSerializer

    def perform_create(self, serializer):

        module_id=self.kwargs.get("pk")
        module_object=get_object_or_404(Module,id=module_id)
        serializer.save(module=module_object,created_by=self.request.user)

class LessonRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=LessonSerializer
    queryset=Lesson.objects.all()


