import json
import requests
from datetime import datetime, timedelta, timezone
from requests.structures import CaseInsensitiveDict

from jwt import (
    JWT,
    jwk_from_dict,
    jwk_from_pem,
)
from jwt.utils import get_int_from_datetime

def main():
    instance = JWT()
    message = {
        # Client ID for non-production
        'iss': '65fbdcfb-4b17-4a6d-996c-db023a3d68db',
        'sub': '65fbdcfb-4b17-4a6d-996c-db023a3d68db',
        'aud': 'https://fhir.epic.com/interconnect-fhir-oauth/oauth2/token',
        'jti': 'f9eaafba-2e49-11ea-8880-5ce0c5aee679',
        # 'iat': get_int_from_datetime(datetime.now(timezone.utc)),
        'exp': get_int_from_datetime(datetime.now(timezone.utc) + timedelta(minutes=2)),
    }
    print(message)
    # Load a RSA key from a PEM file.
    with open('privatekey.pem', 'rb') as fh:
        signing_key = jwk_from_pem(fh.read())

    compact_jws = instance.encode(message, signing_key, alg='RS384')
    print(compact_jws)

    headers = CaseInsensitiveDict()
    headers['Content-Type'] = 'application/x-www-form-urlencoded'

    data = {
      'grant_type': 'client_credentials',
      'client_assertion_type': 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
      'client_assertion': compact_jws
    }
    
    x = requests.post('https://fhir.epic.com/interconnect-fhir-oauth/oauth2/token', headers=headers, data=data)
    print(x.text)
    print(x)
    
    
    
if __name__ == "__main__":
    main()