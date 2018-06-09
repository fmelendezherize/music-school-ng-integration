# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SubjectSerializer, DepartmentSerializer
from .serializers import ProfessorSerializer, ProfessorGetSerializer, ProfessorPostSerializer, ProfessorPutSerializer

from .models import Professor, Subject, Department

# Create your views here.
class SubjectList(APIView):
    def get(self, request, format=None):
        #instruments = Instrument.objects.select_related('department').all()
        subjects = Subject.objects.all()
        if len(subjects) > 0:
            print subjects[0].department.description
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

class DepartmentList(APIView):
    def get(self, request, format=None):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

class ProfessorList(APIView):
    def get(self, request, format=None):
        professors = Professor.objects.all()
        #Must have its own serializer
        serializer = ProfessorGetSerializer(professors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfessorPostSerializer(data=request.data)
        if serializer.is_valid():
            the_response = ProfessorSerializer(serializer.save())
            return Response(the_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfessorDetail(APIView):
    """
    Retrieve, update or delete a professor instance.
    """
    #Lo de arriba aparece en la pagina que genera Django
    def get_object(self, pk):
        try:
            return Professor.objects.get(pk=pk)
        except Professor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        professor = self.get_object(pk)
        serializer = ProfessorGetSerializer(professor)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        professor = self.get_object(pk)
        professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        serializer = ProfessorPutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    