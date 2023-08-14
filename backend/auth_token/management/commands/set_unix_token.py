from django.core.management.base import BaseCommand
from auth_token.models import Token
from auth_token.utils.token_utils import generate_token
import os

class Command(BaseCommand):
    help = 'Generate and set a new JWT token'

    def handle(self, *args, **options):
        new_token = generate_token()
        token = Token.set_new_token('frontend', new_token)
        token_str = token.token.decode('utf-8')
        
        os.environ["BEARER_TOKEN"] = token_str
        
        if os.environ.get('BEARER_TOKEN'):
            return self.stdout.write(self.style.SUCCESS(f'New token set successfully token: {token_str}'))

        self.stderr.write(self.style.ERROR(f'Error setting token: {token_str}\nin the system environment!'))
