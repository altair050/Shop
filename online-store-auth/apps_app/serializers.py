from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from apps_app.models import App


class AppSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True, allow_null=False, allow_blank=False,
                               validators=[UniqueValidator(queryset=App.objects.all())])
    secret = serializers.CharField(required=True, allow_null=False, allow_blank=False, write_only=True)
    is_internal = serializers.BooleanField(read_only=True)

    class Meta:
        model = App
        fields = [
            'id',
            'secret',
            'is_internal',
        ]

    def create(self, validated_data):
        new = App.objects.create(id=validated_data['id'], secret=validated_data['secret'])
        return new


class TokenForAppSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    secret = serializers.CharField(required=True, allow_null=False, allow_blank=False)

    class Meta:
        model = App
        fields = [
            'id',
            'secret',
        ]