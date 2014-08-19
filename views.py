# -*-coding=utf-8-*-

from .oauthprovider import Auth2, ResourceProvider
from django.http import HttpResponse, HttpResponseRedirect


def get_auth_code(request):
    if request.user.is_authenticated():  # for test
        auth = Auth2(request.user)  # Auth2(request.user.id)
        uri = request.get_full_path()
        response = auth.get_authorization_code_from_uri(uri)
        if response.status_code == 302:
            return HttpResponseRedirect(response.headers['Location'])
        return HttpResponse(response.content)


def get_token_code(request):
    data = request.GET.dict()
    response = Auth2(request.user).get_token_from_post_data(data)
    return HttpResponse(response.content)


def get_token_by_client(request):
    data = request.GET.dict()
    response = Auth2(request.user).get_token_by_client(**data)
    return HttpResponse(response.content)


def test_token(request):
    resource = ResourceProvider()
    token_code = request.GET.get('token_code')
    if resource.is_valid_access(token_code, scope=2):
        return HttpResponse('ok')
    return HttpResponse('access is denied')
