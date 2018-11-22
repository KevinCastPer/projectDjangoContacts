from rest_framework import serializers
from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.Field('owner.username')

    class Meta:
        model = Contact
        fields = (
            'id',
            'owner',
            'nameContact',
            'email',
            'phone',
            'message'
            )
