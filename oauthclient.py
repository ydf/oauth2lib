# -*-coding=utf-8-*-

#import urllib

from oauth2lib.client import Client

# client_id = '219866860'
# client_secret = 'e7223b9c0d304ef1f608d205885de632'
# redirect_uri = 'http://yun.peopledu.tk/callback'
# authorization_uri = 'https://api.weibo.com/oauth2/authorize'
# token_uri = 'https://api.weibo.com/oauth2/access_token'


client_id = '123'
client_secret = '123'
redirect_uri = 'http://www.linux.com/callback'
authorization_uri = 'http://127.0.0.1:8000/authorize'
token_uri = 'http://127.0.0.1:8000/access_token'

sina_oauth = Client(client_id, client_secret,
                    redirect_uri, authorization_uri, token_uri)

# App Key：219866860
# App Secret：e7223b9c0d304ef1f608d205885de632


def updata(content):
    uri = 'https://api.weibo.com/2/statuses/update.json'
    msg = {}
    msg['access_token'] = '2.00FA9M_C0g6XsO9a779757cdPt4RGE'
    msg['status'] = content
    # print data
    return sina_oauth.http_post(uri, msg).content


class test(object):

    """docstring for test"""

    def __init__(self):
        super(test, self).__init__()
        self.arg = 1
        print self.arg
        self.arg += 1
        print self.arg


if __name__ == '__main__':
    # print dir(sina_oauth)
    print sina_oauth.get_authorization_code_uri()  # get auth uri
   # print updata('ceshi  zidong')
    # print sina_oauth.get_token('b1163ba1cc83793dc2efc684501e9431')
    print sina_oauth.get_token('BkH1tNm9rre40ocOPdQrRncKRQzWVePFfLzAfefw')
