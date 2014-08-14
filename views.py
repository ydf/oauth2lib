# -*-coding=utf-8-*-

from . import oauthprovider

def provider_code(request):
    kwargs = request.GET
    return oauthprovider.get_authorization_code(*kwargs)



