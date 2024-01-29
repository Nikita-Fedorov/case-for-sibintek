from rest_framework import serializers
from myself.models import Myself


class MyselfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myself
        fields = '__all__'
