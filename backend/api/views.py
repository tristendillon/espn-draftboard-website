from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import PostPermission
from .serializers import *

class PostTest(APIView):
    permission_classes = [PostPermission]
    
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer
        if serializer.is_valid():
            return Response({'status': 'success'})
        
        return Response({'status': 'error'})