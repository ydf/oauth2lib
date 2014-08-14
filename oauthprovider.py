# -*-coding=utf-8-*-

from oauth2lib.provider import AuthorizationProvider
from oauth.models import ClientId

class Auth2(AuthorizationProvider):
    """docstring for Auth2"""
    def __init__(self):
        super(Auth2, self).__init__()
        
    def validate_client_id(self, client_id):
        #Return True or False
        if ClientId.objects.get(client_id=client_id):
            return True
        return False

    def validate_client_secret(self, client_id, client_secret):
        # Return True or False
        if ClientId.objects.get(client_id=client_id)['client_secret'] == client_secret:
            return True
        return False

    def validate_scope(self, client_id, scope):
        # Return True or False
        return True

    def validate_redirect_uri(self, client_id, redirect_uri):
        # Return True or False
        return True

    def validate_access(self):  # Use this to validate your app session user
        # Return True or False
        return True
    def from_authorization_code(self, client_id, code, scope):
        # Return mixed data or None on invalid
        return True
    def from_refresh_token(self, client_id, refresh_token, scope):
        # Return mixed data or None on invalid
        return True

    def persist_authorization_code(self, client_id, code, scope):
        # Return value ignored
        return True

    def persist_token_information(self, client_id, scope, access_token,
                              token_type, expires_in, refresh_token,
                              data):
        # Return value ignored
        return True

    def discard_authorization_code(self, client_id, code):
        # Return value ignored
        return True

    def discard_refresh_token(self, client_id, refresh_token):
        # Return value ignored
        return True


if __name__ == '__main__':
    # print dir(sina_oauth)
    print sina_oauth.get_authorization_code_uri() # get auth uri
   # print updata('ceshi  zidong')
    #print sina_oauth.get_token('b1163ba1cc83793dc2efc684501e9431')

