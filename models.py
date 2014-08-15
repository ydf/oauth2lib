# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from django.conf import settings

# class UserData(models.Model):
#     user_name = models.CharField(max_length=255, unique=True)
#     user_email = models.CharField(max_length=255, unique=True, db_index=True)
#     user_mobile = models.IntegerField(
#         max_length=300, unique=True, db_index=True)
#     register_time = models.DateTimeField(
#         null=True, blank=True, auto_now_add=True)

#     class Meta:
#         db_table = u'userdb'

AUTH_USER = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ClientId(models.Model):
    client_id = models.CharField(max_length=255, primary_key=True)
    user_id = models.ForeignKey(AUTH_USER)
    client_secret = models.CharField(max_length=30)
    #client_permit = models.IntegerField(null=True, blank=True)
    client_permit = models.IntegerField()
    redirect_uri = models.CharField(max_length=30,)

    class Meta:
        db_table = u'client'


class Token(models.Model):
    user_id = models.ForeignKey(AUTH_USER)  # user give client's permit
    auth_code = models.CharField(max_length=255, db_index=True, unique=True)  # default 300s
    token_code = models.CharField(max_length=255, db_index=True, unique=True)
    client_id =  models.CharField(max_length=255)
    user_permit = models.IntegerField()
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(null=True, blank=True)
    token_expires = models.IntegerField()    # token timeout

    class Meta:
        db_table = u'token'
