import os
import logging
from dotenv import load_dotenv
from rest_framework import permissions
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

logger = logging.getLogger(__name__)
load_dotenv()
SYSTEM_ENV = os.environ.get("SYSTEM_ENV", None)

# TODO: update the following so it holds auth token fed
# into the instantiation of the cli client. It'll fetch
# the existing auth tokens for a user based on user id
# it'll return an authentication status if the initialized token
# matches the users token in the admin panel. Thus allowing
# the user to make subsequent request to each of the cli packages
# i.e `Apollo.use` or `Apollo.connect`, `Apollo.detectText`
class ExternalEnvironmentPermission(permissions.BasePermission):

    if SYSTEM_ENV == "DEVELOPMENT":
        token = os.environ.get("DEV_TOKEN")
    elif SYSTEM_ENV == "PRODUCTION":
        token = os.environ.get("PROD_TOKEN")

    def has_permission(self, request, view):
        auth_token = request.META.get("HTTP_AUTHORIZATION")
        return auth_token == f"Token {self.token}"


class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

    # NOTE: overriding due to comment found in auth/views:IsAuthenticatedView.
    # Override to grab user from session context.
    @staticmethod
    def get_user(user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist as err:
            logger.info("User not found, %s", user_id)
            raise err
