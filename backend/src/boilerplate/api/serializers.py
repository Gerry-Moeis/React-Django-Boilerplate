from rest_framework import serializers

from boilerplate.models import *

class BoilerplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boilerplate
        fields = '__all__'