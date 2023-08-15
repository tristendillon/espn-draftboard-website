from rest_framework.permissions import BasePermission

from auth_token.models import Token
from django.utils.encoding import smart_bytes 

class PostPermission(BasePermission):
    def has_permission(self, request, view):
        
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if not authorization_header:
            return False      
        
        try:
            # Set _ to 'Bearer', token to the decoded token
            _, token = authorization_header.split()
            
            # encode the token to bytes
            byte_token = smart_bytes(token, encoding='utf-8')
            
            # query the tokens for if there is a token with the same bytes
            token = Token.objects.filter(token=byte_token).first()
            
            if not token:
                return False
            
            if token.token_type == 'extension':
                return True 
            else:
                return False 
        except ValueError:
            return False 
    
    
class GetPermission(BasePermission):
    def has_permission(self, request, view):
        
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if not authorization_header:
            return False      
        
        try:
            # Set _ to 'Bearer', token to the decoded token
            _, token = authorization_header.split()
            
            # encode the token to bytes
            byte_token = smart_bytes(token, encoding='utf-8')
            
            # query the tokens for if there is a token with the same bytes
            token = Token.objects.filter(token=byte_token).first()
            
            if not token:
                return False
            
            if token.token_type == 'frontend':
                return True 
            else:
                return False 
        except ValueError:
            return False 