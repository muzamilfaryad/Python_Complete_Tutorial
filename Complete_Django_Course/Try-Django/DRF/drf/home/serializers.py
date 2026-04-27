from rest_framework import serializers
from .models import Person , Color


#if you want to create a serializer for login purpose then 
# you can use serializers.Serializer instead 
# of serializers.ModelSerializer
class loginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        # fields =  ['color_name']
        fields =  ['color_name','id']

class PersonSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
  #custom method field 
    #country = serializers.SerializerMethodField()
    color_info = serializers.SerializerMethodField()
    class Meta:
        model = Person
        #fields = ['name', 'age']
        fields = '__all__'
        #exclude = ['id']
       # depth = 1


#custom method 
    # def get_country(self, obj):
    def get_color_info(self, obj):
        if obj.color is None:
            return None
       # return 'Pakistan'
        return {'color_name': obj.color.color_name , 'hex_code' : '#000'}



    # def validate(self, data):
    #     print('********************')
    #     print(data)
    #     return data
    #     print('********************')





    #    def validate_age(self, age):
    #     print('********************')
    #     print(age)
    #     return age
    #     print('********************')



#Validation is the process of checking if the data is valid or not.

    def validate(self, data):

        special_characters = "!@#$%^&*()-+?_=,<>/"
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError("Name contains special characters")



        # if data['age'] < 10:
        #     raise serializers.ValidationError("Age must be greater than 10")
        # return data


        if data.get('age') and data['age'] < 10:
            raise serializers.ValidationError("Age must be greater than 10")
        return data



from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already exists")

        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already exists")

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user



