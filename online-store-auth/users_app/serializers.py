from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_superuser']


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(allow_null=False, allow_blank=False, min_length=6, max_length=50, write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

    def create(self, validated_data):
        new = User.objects.create(username=validated_data['username'])
        new.set_password(validated_data['password'])
        new.save()
        return new


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(allow_null=False, allow_blank=False, min_length=6, max_length=50, write_only=True)
    password_confirm = serializers.CharField(allow_null=False, allow_blank=False, min_length=6, max_length=50,
                                             write_only=True)
    old_password = serializers.CharField(allow_null=False, allow_blank=False, max_length=50, write_only=True)

    class Meta:
        model = User
        fields = [
            'password',
            'password_confirm',
            'old_password',
        ]

    def update(self, instance: User, validated_data):
        if not instance.check_password(validated_data['old_password']):
            raise serializers.ValidationError('Текущий пароль введен неверно')
        if validated_data['password'] != validated_data['password_confirm']:
            raise serializers.ValidationError('Пароли не сходятся')
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
