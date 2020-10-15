from rest_framework import serializers
from billing_app.models import Billing


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = ['payment_method', 'address', 'telephone_number', 'uuid']

    def create(self, validated_data):
        new = Billing(**validated_data)
        new.save()
        return new


