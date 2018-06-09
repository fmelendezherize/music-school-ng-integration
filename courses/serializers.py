from rest_framework import serializers
from .models import Course
from professors.models import Professor, Subject
from students.models import Student

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        depth = 1
        fields='__all__'

class CourseWriteSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    idprofessor = serializers.IntegerField()
    idsubject = serializers.IntegerField()

    def create(self, validated_data):
        professor = Professor.objects.get(pk=validated_data['idprofessor'])
        subject = Subject.objects.get(pk=validated_data['idsubject'])
        new_course = Course.objects.create(name=validated_data['name'], 
            professor=professor, subject=subject, 
            description=validated_data['description'])
        return new_course

    def update(self, instance, validated_data):
        professor = Professor.objects.get(pk=validated_data['idprofessor'])
        instance.professor = professor
        subject = Subject.objects.get(pk=validated_data['idsubject'])
        instance.subject = subject
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class RegisterStudentSerializer(serializers.Serializer):
    idstudent = serializers.IntegerField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        my_student = Student.objects.get(pk=validated_data['idstudent'])
        instance.register_student(my_student)
        instance.save()
        return instance

class EnrollStudentSerializer(serializers.Serializer):
    idstudent = serializers.IntegerField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        instance.enroll_student(validated_data['idstudent'])
        return instance

class RejectStudentSerializer(serializers.Serializer):
    idstudent = serializers.IntegerField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        instance.reject_student(validated_data['idstudent'])
        instance.save()
        return instance