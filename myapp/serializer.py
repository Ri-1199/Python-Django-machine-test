from rest_framework import serializers
from .models import Client


import re
from django.template.defaultfilters import slugify

class ClientSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = '__all__'
        # exclude = ['created_at']

    def get_slug(self, obj):
        return slugify(obj.client_name)

    def validate_todo_title(self , data):
        if data:
            client_name = data
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

            if len(client_name) < 3:
                raise serializers.ValidationError('client_name must be more than 3 chars')

            if not regex.search(client_name) == None:
                raise serializers.ValidationError('client_name cannot contains special characters')

        return data






