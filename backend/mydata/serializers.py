from rest_framework import serializers

from .models import Mydata

class MydataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mydata
        fields = "__all__"