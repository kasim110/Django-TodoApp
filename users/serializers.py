from rest_framework import serializers
from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):

    message = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'first_name','last_name','mobile','email','city','state','country','zipcode','address',
            'password','message'
        ]

        extra_kwargs = {'password' : {'write_only':True}}

    def get_message(self, obj):
        return "Thank you for registering. Please verify your mobile number before continuing."
    
    def validate_mobile(self, value):
        qs = User.objects.filter(mobile=value)

        if qs.exists():
            raise serializers.ValidationError("User with this mobile number already registered.")
        return value
    
    def create(self, validated_data):
        user_obj = User.objects.create_new_user(**validated_data, is_active=True)

        return user_obj
