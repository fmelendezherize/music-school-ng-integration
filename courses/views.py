# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from .serializers import CourseSerializer, CourseWriteSerializer, RegisterStudentSerializer, EnrollStudentSerializer, RejectStudentSerializer

from .models import Course

# # Create your views here.
# class CourseList(APIView):
#     def get(self, request, format=None):
#         courses = Course.objects.all()
#         #Must have its own serializer
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = CourseWriteSerializer(data=request.data)
#         if serializer.is_valid():
#             the_response = CourseSerializer(serializer.save())
#             return Response(the_response.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CourseDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         course = self.get_object(pk)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)

#     def delete(self, request, pk, format=None):
#         course = self.get_object(pk)
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def put(self, request, pk, format=None):
#         course = self.get_object(pk)
#         serializer = CourseWriteSerializer(course, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseViewSet(viewsets.ViewSet):

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def list(self, request):
        courses = Course.objects.all()
        #Must have its own serializer
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CourseWriteSerializer(data=request.data)
        if serializer.is_valid():
            the_response = CourseSerializer(serializer.save())
            return Response(the_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def update(self, request, pk=None):
        course = self.get_object(pk)
        serializer = CourseWriteSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # @list_route(methods=['put'])
    # def register(self, request):
    #     pass

    @detail_route(methods=['post'])
    def register(self, request, pk=None):
        course = self.get_object(pk)
        serializer = RegisterStudentSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['post'])
    def enroll(self, request, pk=None):
        course = self.get_object(pk)
        serializer = EnrollStudentSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['delete'])
    def reject(self, request, pk=None):
        course = self.get_object(pk)
        serializer = RejectStudentSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
