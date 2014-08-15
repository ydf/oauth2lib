# -*-coding=utf-8-*-

from .oauthprovider import Auth2
from django.http import HttpResponse


def get_auth_code(request):
    kwargs = request.GET
    if request.user.is_authenticated():  # for test
        auth = Auth2(request.user)  # Auth2(request.user.id)
        uri = request.get_full_path()
        response = auth.get_authorization_code_from_uri(uri)
        #print  response.headers
        return HttpResponse(response.status_code)


def function():
    pass
