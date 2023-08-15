from rest_framework import serializers
from .models import *

class PostDraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Draft
        fields = '__all__' 

class PostPickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pick
        fields = '__all__' 
        
class PostTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__' 
        
class PostTimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = 'all'