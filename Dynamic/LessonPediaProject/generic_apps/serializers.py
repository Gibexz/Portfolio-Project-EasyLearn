from rest_framework import serializers
from .models import ClientReportAbuse
from .models import TutorReportAbuse


class ClientReportAbuseSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = ClientReportAbuse
        fields = '__all__'
    

class TutorReportAbuseSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = TutorReportAbuse
        fields = '__all__'