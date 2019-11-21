from datetime import datetime, timedelta
from base64 import urlsafe_b64encode
import json
import hmac
import hashlib
from run import app

def create_token(username):
    expiration = datetime.now() + timedelta(days=1)
    payload = {"username" : username, "expiration" : str(expiration)}
    payload = json.dumps(payload).encode('utf-8')
    encoded_payload = urlsafe_b64encode(payload)
    secret_key = app.config['SECRET_KEY']
    signature = hmac.new(secret_key.encode('utf-8'),encoded_payload,hashlib.sha256).digest()
    encoded_signature = urlsafe_b64encode(signature)
    token = '{}.{}'.format(encoded_payload.decode('utf-8'),encoded_signature.decode('utf-8'))
    return token