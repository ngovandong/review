from rest_framework import serializers
from .models import CustomUser
from trello.models import Workspace


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'address', 'phone_number', 'avatar',
                  'thumbnail', 'role', 'password', ]
        read_only_fields = ['role', 'thumbnail']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()
        workspace = Workspace.objects.create(
            name=instance.get_full_name()+" workspace", owner_id=instance.id)
        workspace.users.add(instance)
        workspace.save()
        return instance


class PowerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'address', 'phone_number', 'avatar',
                  'thumbnail', 'role', 'password', ]
        read_only_fields = ['role', 'thumbnail']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data["role"] = "PU"
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        workspace = Workspace.objects.create(
            name=instance.get_full_name()+" workspace", owner_id=instance.id)
        workspace.users.add(instance)
        workspace.save()
        return instance
