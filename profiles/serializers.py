from rest_framework.serializers import (
    CharField, ModelSerializer, Serializer,
)

from profiles.models import UserProfile


class HelloSerializer(Serializer):
    name = CharField(max_length=10)


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style' : {'input_type' : 'password'}
            }
        }

    def create(self, validated_data):
        """"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)