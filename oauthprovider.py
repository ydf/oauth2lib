# -*-coding=utf-8-*-

from oauth2lib.provider import AuthorizationProvider
from oauth.models import ClientId, Token


class Auth2(AuthorizationProvider):

    """docstring for Auth2"""

    def __init__(self, user):
        super(Auth2, self).__init__()
        self.user = user

    def validate_client_id(self, client_id):
        # Return True or False
        return ClientId.objects.filter(client_id=client_id) is not None

    def validate_client_secret(self, client_id, client_secret):
        # Return True or False
        client = ClientId.objects.filter(client_id=client_id)
        if client is not None and client.values()[0]['client_secret'] == client_secret:
            return True
        return False

    def validate_scope(self, client_id, scope):
        # Return True or False
        client = ClientId.objects.filter(client_id=client_id)
        if scope is '':
            scope = 2
        if client is not None and client.values()[0]['client_permit'] >= scope:
            return True
        return False

    def validate_redirect_uri(self, client_id, redirect_uri):
        # Return True or False
        client = ClientId.objects.filter(client_id=client_id)
        print type(redirect_uri)
        print client.values()[0]['redirect_uri']
        if client is not None and client.values()[0]['redirect_uri'] == redirect_uri:
            return True
        return False

    def validate_access(self):  # Use this to validate your app session user
        # Return True or False
        # test for default True
        return True

    def from_authorization_code(self, client_id, code, scope):
        # Return mixed data or None on invalid
        return True

    def from_refresh_token(self, client_id, refresh_token, scope):
        # Return mixed data or None on invalid
        return True

    def persist_authorization_code(self, client_id, code, scope):
        # Return value ignored
        if scope is '':
            scope = 2
        auth_code = Token(
            client_id=client_id, auth_code=code, user_permit=scope, user_id=self.user, token_expires=30)
        auth_code.save()
        # u can use this:Token.objects.create(client_id=client_id, code=code,
        # user_permit=scope)
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
    print sina_oauth.get_authorization_code_uri()  # get auth uri
    # print updata('ceshi  zidong')
    # print sina_oauth.get_token('b1163ba1cc83793dc2efc684501e9431')
