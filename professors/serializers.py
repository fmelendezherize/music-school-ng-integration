from rest_framework import serializers
from .models import Professor
from .models import Subject, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        depth = 1
        fields = ('id','name','description','subject_deparment')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        #depth = 1 #show deparment object as related data. Nested Serialization
        fields = ('id','name','description', 'department')

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(read_only=True)

class ProfessorSerializer(serializers.ModelSerializer):
    #Asi puedo serializar algun objeto Nested
    #user = UserSerializer()
    #Asi puedo serializar algun nested field o function
    email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Professor
        #fields='__all__'
        #Aqui no usamos depth porque no son tan inofensivos como creiamos, afectan el POST
        fields = ('id','names','lastnames', 'identification_number', 'phone', 'address', 'skills', 'subjects', 'email') 

class ProfessorGetSerializer(ProfessorSerializer):
    #Serializador solo para GET y simula un depth=1
    subjects = SubjectSerializer(many=True, read_only=True)

class ProfessorPostSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)
    idofSubjects = serializers.ListField(
        child=serializers.IntegerField()
    )

    def create(self, validated_data):
        return Professor.objects.create_professor(
            email=validated_data['email'], password=validated_data['password'], 
            idsOfSubjects=validated_data['idofSubjects'])

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.created = validated_data.get('password', instance.password)
        instance.save()
        return instance

class ProfessorPutSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)
    names = serializers.CharField(max_length=200)
    lastnames = serializers.CharField(max_length=200)
    identification_number = serializers.CharField(max_length=40)
    phone = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=40)
    skills = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Professor.objects.register_professor(email=validated_data['email'], password=validated_data['password'],
               names=validated_data['names'], lastnames=validated_data['lastnames'], identification_number=validated_data['identification_number'],
               phone=validated_data['phone'], address=validated_data['address'], skills=validated_data['skills'])

    def update(self, instance, validated_data):
        # instance.email = validated_data.get('email', instance.email)
        # instance.password = validated_data.get('password', instance.password)
        # instance.names = validated_data.get('names', instance.names)
        # instance.lastnames = validated_data.get('lastnames', instance.lastnames)
        # instance.identification_number = validated_data.get('identification_number', instance.identification_number)
        # instance.phone = validated_data.get('phone', instance.phone)
        # instance.address = validated_data.get('address', instance.address)
        # instance.skills = validated_data.get('skills', instance.skills)
        # instance.save()
        # return instance
        pass
