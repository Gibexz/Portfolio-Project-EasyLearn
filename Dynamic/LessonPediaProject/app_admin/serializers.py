from rest_framework import serializers
from client.models import Client
from tutor.models import Tutor

class ClientSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Client
        fields = '__all__'


class TutorSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Tutor
        fields = '__all__' # You can specify the fields explicitly if needed
