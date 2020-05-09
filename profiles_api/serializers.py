from rest_framework import serializers

from profiles_api import models
from profiles_api.validators import validate_alpha


class HelloSerializers(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on','updated_on')

        extra_kwargs = {
            'user_profile':{'read_only':True}
        }

class EmpTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EmpTable
        fields = ('id','emp_id','emp_firstname','emp_lastname','emp_active','emp_dept','created_on')
        extra_kwargs = {'emp_id' : {'read_only' : False}}

class DeptTableSerializer(serializers.ModelSerializer):

    dept_name = serializers.CharField(min_length=10)
    dept_name = serializers.CharField(validators=[validate_alpha])

    class Meta:
        model = models.DeptTable
        fields = ('id','dept_id','dept_name','dept_active','created_on')
