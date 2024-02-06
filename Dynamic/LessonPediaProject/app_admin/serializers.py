from rest_framework import serializers
from client.models import Client, Transaction
from tutor.models import Tutor, Subject
from generic_apps.models import Contract

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

class TransactionSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Transaction
        fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Contract
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Subject
        fields = '__all__'