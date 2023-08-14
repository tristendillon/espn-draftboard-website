import secrets

jwt_secret_key = secrets.token_hex(32)  # Generates a 64-character hex key

print(jwt_secret_key)