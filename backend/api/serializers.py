from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Draft
        fields = '__all__' 

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