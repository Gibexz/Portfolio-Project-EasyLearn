from rest_framework import serializers
from client.models import Client
# , ClientReportAbuse
from tutor.models import Tutor
# , TutorReportAbuse

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


# class ClientReportAbuseSerializer(serializers.ModelSerializer):
#     """"""
#     class Meta:
#         model = ClientReportAbuse
#         fields = '__all__'
    

# class TutorReportAbuseSerializer(serializers.ModelSerializer):
#     """"""
#     class Meta:
#         model = TutorReportAbuse
#         fields = '__all__'