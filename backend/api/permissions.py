from rest_framework.permissions import BasePermission

from auth_token.models import Token
from django.utils.encoding import smart_bytes 

class PostPermission(BasePermission):
    def has_permission(self, request, view):
        print("AUTHING")
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        print(authorization_header)
        if not authorization_header:
            return False      
        
        try:
            _, token = authorization_header.split()
            byte_token = smart_bytes(token, encoding='utf-8')
            token = Token.objects.filter(token=byte_token).first()
            print(token.token_type)
            
            if not token:
                return False
            
            if token.token_type == 'extension':
                return True 
            else:
                return False 
        except ValueError:
            return False 