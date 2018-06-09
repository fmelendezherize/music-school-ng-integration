from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    password = serializers.CharField(max_length=10, write_only=True)
    in_email = serializers.EmailField(write_only=True)

    class Meta:
        model = Student
        #fields='__all__'
        #Aqui no usamos depth porque no son tan inofensivos como creiamos, afectan el POST
        fields = ('id','names','lastnames', 'identification_number', 'phone', 'address', 'date_birth', 'email', 'password', 'in_email') 
    
    def create(self, validated_data):
        return Student.objects.create_student(
            email=validated_data['in_email'],
            password=validated_data['password'],
            names=validated_data['names'],
            lastnames=validated_data['lastnames'],
            identification_number=validated_data['identification_number'],
            phone=validated_data['phone'],
            address=validated_data['address'],
            date_birth=validated_data['date_birth'])

    def update(self, instance, validated_data):
        instance.user.email = validated_data.get('in_email', instance.user.email)
        instance.names = validated_data.get('names', instance.names)
        instance.lastnames = validated_data.get('lastnames', instance.lastnames)
        instance.identification_number = validated_data.get('identification_number', instance.identification_number)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.date_birth = validated_data.get('date_birth', instance.date_birth)
        instance.user.set_password(validated_data['password'])
        instance.user.save()
        instance.save()
        return instance

