import jwt
import secrets
from datetime import datetime, timedelta
from django.conf import settings

def generate_token():
    payload = {
        'custom_id': secrets.token_urlsafe(16),
        'exp': datetime.utcnow() + timedelta(days=14)
    }
    return jwt.encode(payload, settings.JWT_AUTH['JWT_SECRET_KEY'], algorithm='HS256')