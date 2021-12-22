from rest_framework import serializers
from about.models import WishMessage


class WishMessageSerializer(serializers.ModelSerializer):
    WISH_LIMIT = 3
    ALL_PREVIOUS_KEY = 'all_previous'

    def create(self, validated_data):
        email = validated_data.get('email', None)
        if email:
            wishes = WishMessage.objects.filter(email=email)
            if wishes.count() >= self.WISH_LIMIT:
                raise serializers.ValidationError('You send more than 3 wishes!')
        return WishMessage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.title)
        instance.last_name = validated_data.get('last_name', instance.description)
        instance.message = validated_data.get('message', instance.body)
        instance.email = validated_data.get('email', instance.author_id)
        instance.allow_mailing = validated_data.get('allow_mailing', instance.author_id)

        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request_method = self.context.get('request_method', None)
        if self.context.get(self.ALL_PREVIOUS_KEY, True) and request_method == 'POST':
            all_previous_by_email = WishMessage.objects.filter(email=instance.email).exclude(id=instance.id) # to show user all his previous wishes
            wishes_serializer = WishMessageSerializer(all_previous_by_email, many=True, context={self.ALL_PREVIOUS_KEY: False})
            representation[self.ALL_PREVIOUS_KEY] = wishes_serializer.data
        
        return representation

    class Meta:
        model = WishMessage
        fields = '__all__'
