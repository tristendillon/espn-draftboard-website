import jwt
import secrets
from datetime import datetime, timedelta
from django.conf import settings
from django.utils.encoding import smart_bytes 

def generate_token():
    payload = {
        'custom_id': secrets.token_urlsafe(16),
        'exp': datetime.utcnow() + timedelta(days=90)
    }
    return smart_bytes(jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256'))