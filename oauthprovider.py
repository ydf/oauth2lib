# -*-coding=utf-8-*-

import time

from oauth2lib.provider import AuthorizationProvider
from oauth.models import ClientId, Token, AuthCode


class Auth2(AuthorizationProvider):

    """default scope = 2,"""

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
        if client is not None and client.values()[0]['redirect_uri'] == redirect_uri:
            return True
        return False

    def validate_access(self):  # Use this to validate your app session user
        # Return True or False
        # test for default True
        return True  # at django, it's has validate user.

    def from_authorization_code(self, client_id, code, scope):
        # Return mixed data or None on invalid
        if scope == '':
            scope = 2
        client = AuthCode.objects.filter(auth_code=code)
        utc_time = client.values()[0]['creat_time']
        if client is not None and client.values()[0]['user_permit'] >= scope:
            utc_time = client.values()[0]['creat_time'].timetuple()
            time_stamp = int(time.mktime(utc_time))
            if time_stamp > int(time.time()) - 3600:
                return {'user_id': client.values()[0]['user_id_id']}
        return None

    def from_refresh_token(self, client_id, refresh_token, scope):
        # Return mixed data or None on invalid +
        return None

    def persist_authorization_code(self, client_id, code, scope):
        # Return value ignored
        if scope is '':
            scope = 2
        auth_code = AuthCode(client_id=client_id,
                             auth_code=code,
                             user_permit=scope,
                             user_id=self.user,)
        auth_code.save()
        # u can use this:Token.objects.create(client_id=client_id, code=code,
        # user_permit=scope)

    def persist_token_information(self, client_id, scope, access_token,
                                  token_type, expires_in, refresh_token,
                                  data):
        # Return value ignored
        # save token data
        # now don't support refresh token
        if scope is '':
            scope = 2

        token_code = Token(client_id=client_id,
                           user_permit=scope,
                           token_code=access_token,
                           token_expires=expires_in,
                           user_id=data['user_id'],
                           )
        token_code.save()
        return True

    def discard_authorization_code(self, client_id, code):
        # Return value ignored
        # remove client_id and code
        AuthCode.objects.filter(auth_code=code).delete()
        return True

    def discard_refresh_token(self, client_id, refresh_token):
        # Return value ignored
        return True

    def get_token_by_client(self,
                            grant_type,
                            client_id,
                            client_secret,
                            redirect_uri,
                            **params):
        """Generate access token HTTP response.
        :param grant_type: Desired grant type. Must be "clientcredentials".
        :type grant_type: str
        :param client_id: Client ID.
        :type client_id: str
        :param client_secret: Client secret.
        :type client_secret: str
        :param redirect_uri: Client redirect URI.
        :type redirect_uri: str
        :rtype: requests.Response
        """

        # Ensure proper grant_type
        if grant_type != 'clientcredentials':
            return self._make_json_error_response('unsupported_grant_type')

        # Check conditions
        is_valid_client_id = self.validate_client_id(client_id)
        is_valid_client_secret = self.validate_client_secret(client_id,
                                                             client_secret)
        is_valid_redirect_uri = self.validate_redirect_uri(client_id,
                                                           redirect_uri)

        scope = params.get('scope', '')
        is_valid_scope = self.validate_scope(client_id, scope)

        # Return proper error responses on invalid conditions
        if not (is_valid_client_id and is_valid_client_secret):
            return self._make_json_error_response('invalid_client')

        if not is_valid_redirect_uri:
            return self._make_json_error_response('invalid_grant')

        if not is_valid_scope:
            return self._make_json_error_response('invalid_scope')

        # Generate access tokens once all conditions have been met
        access_token = self.generate_access_token()
        token_type = self.token_type
        expires_in = self.token_expires_in
        refresh_token = self.generate_refresh_token()

        # Save information to be used to validate later requests
        self.persist_token_information(client_id=client_id,
                                       scope=scope,
                                       access_token=access_token,
                                       token_type=token_type,
                                       expires_in=expires_in,
                                       refresh_token=refresh_token,
                                       data=None)

        # Return json response
        return self._make_json_response({
            'access_token': access_token,
            'token_type': token_type,
            'expires_in': expires_in,
            'refresh_token': refresh_token
        })


class ResourceProvider(object):

    """verify token"""

    def __init__(self):
        super(ResourceProvider, self).__init__()

    def is_valid_access(self, token_code, scope):
        """valid time of token and scope of api """
        token = Token.objects.filter(token_code=token_code)
        if token is not None:
            token_values = token.values()[0]
            token_expires = token_values['token_expires']
            utc_time = token_values['creat_time'].timetuple()
            time_stamp = int(time.mktime(utc_time))
            if int(time.time()) - int(token_expires) < time_stamp \
                    and token_values['user_permit'] >= scope:
                return True
        return False


if __name__ == '__main__':
    # print dir(sina_oauth)
    # print sina_oauth.get_authorization_code_uri()  # get auth uri
    # print updata('ceshi  zidong')
    print 'ok'
    # 127.0.0.1:8000/access_token?client_id=123&client_secret=123&grant_type=authorization_code&redirect_uri=http%3A%2F%2Fwww.linux.com%2fcallback&code=7nsyBqhfwEDN5ndF6Vw289wOt8R3OljpHIiz4EKW
    # 127.0.0.1:8000/access_token2?client_id=123&client_secret=123&grant_type=clientcredentials&redirect_uri=http%3A%2F%2Fwww.linux.com%2fcallback&code=BkH1tNm9rre40ocOPdQrRncKRQzWVePFfLzAfefw