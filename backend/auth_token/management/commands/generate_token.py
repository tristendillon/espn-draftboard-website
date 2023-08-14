from django.core.management.base import BaseCommand
from auth_token.models import Token
from auth_token.utils.token_utils import generate_token

class Command(BaseCommand):
    help = 'Generate and set a new JWT token'
    def add_arguments(self, parser):
        parser.add_argument('token_type', type=str, help='Generates either a frontend or extension token')

    
    def handle(self, *args, **options):
        token_type = options['token_type']
        if token_type != 'frontend' and token_type != 'extension':
            self.stderr.write(self.style.ERROR('Invalid token type: {0}'.format(token_type)))
            return self.stdout.write(self.style.SQL_TABLE('\nOptions: frontend and extension!'))
            
        new_token = generate_token()
        token = Token.set_new_token(token_type, new_token)
        token_str = token.token.decode('utf-8')
        self.stdout.write(self.style.SUCCESS(f'New {token_type} token set successfully: {token_str}'))
