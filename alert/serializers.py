from rest_framework import serializers
from .models import *



class BirthdaySerializer(serializers.ModelSerializer):
	class Meta:
		model = Birthday
		fields = '__all__'


class MothersDaySerializer(serializers.ModelSerializer):
	class Meta:
		model = MothersDay
		fields = '__all__'

class MarriageAnniversarySerializer(serializers.ModelSerializer):
	class Meta:
		model = MarriageAnniversary
		fields = '__all__'

class RelationshipAnniversarySerializer(serializers.ModelSerializer):
	class Meta:
		model = RelationshipAnniversary
		fields = '__all__'