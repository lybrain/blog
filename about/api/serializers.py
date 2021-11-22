from rest_framework import serializers
from about.models import WishMessage


class WishMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishMessage
        fields = '__all__'
