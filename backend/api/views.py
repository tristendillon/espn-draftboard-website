from django.shortcuts import get_object_or_404
from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .permissions import PostPermission
from .serializers import *
from .models import *
        
class PostDraftView(APIView):
    permission_classes = [PostPermission,]
    
    def post(self, request):
        serializer = PostDraftSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            
            draft = Draft.objects.create(
                id = f'{data.get("id")} - {datetime.datetime.now().year}',
                teams = data.get('teams'),
                roster_spots = data.get('roster_spots'),
                name = data.get('name'),
            )
            
            serialized_draft = PostDraftSerializer(draft)
            return Response(data=serialized_draft.data, status=status.HTTP_201_CREATED )
            
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetDraftView(APIView):
    pass


class PostPickView(APIView):
    permission_classes = [PostPermission,]
    
    def post(self, request):
        if not (draft_id := request.data.get('draft_id')):
            return Response({'error': 'draft_id must be present in the request'}, status= status.HTTP_400_BAD_REQUEST)
        
        serializer = PostPickSerializer(data=request.data)
        
        if serializer.is_valid():
            data = serializer.validated_data
            draft = get_object_or_404(Draft, pk = draft_id)
            
            icon = data.get('icon', DEFAULT_PICK_ICON)
            
            pick = Pick.objects.create(
                name = data.get('name'),
                icon = icon,
                football_team = data.get('football_team'),
                pick_round = data.get('pick_round'),
                pick_number = data.get('pick_number'),
                position = data.get('position'),
                draft_id = draft
            )
            
            serialized_pick = PostPickSerializer(pick)
            return Response(data=serialized_pick.data, status=status.HTTP_201_CREATED )
            
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetPickView(APIView):
    pass
    
    
    
class PostTeamView(APIView):
    permission_classes = [PostPermission,]
    
    def post(self, request):
        if not (draft_id := request.data.get('draft_id')):
            return Response({'error': 'draft_id must be present in the request'}, status= status.HTTP_400_BAD_REQUEST)
        
        serializer = PostTeamSerializer(data=request.data)
        
        if serializer.is_valid():
            data = serializer.validated_data
            draft = get_object_or_404(Draft, pk= draft_id)
            
            team_image =  data.get('team_image', DEFAULT_TEAM_ICON)
            
            team = Team.objects.create(
                name = data.get('name'),
                draft_id = draft,
                team_image = team_image,
            )
            
            serialized_team = PostTeamSerializer(team)
            return Response(data=serialized_team.data, status=status.HTTP_201_CREATED )
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class GetTeamView(APIView):
    pass
    