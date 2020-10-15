from rest_framework.permissions import BasePermission
from gateway_app.requesters.authrequester import AuthRequester
from gateway_app.requesters.requester import Requester


class BaseApiRequestError(Exception):
    def __init__(self, message: str = 'BaseApiRequestError was raised'):
        self.message = message

    def __str__(self):
        return self.message


class BaseAuthPermission(BasePermission):
    def _get_token_from_request(self, request):
        return Requester().get_token_from_request(request)


class IsAuthenticated(BaseAuthPermission):
    def has_permission(self, request, view):
        print('11')
        try:
            token = self._get_token_from_request(request)
            print('22')
            if token is None:
                return False
            print(f'check: {AuthRequester().is_token_valid(token)[1]}')
            return AuthRequester().is_token_valid(token)[1]
            print('33')
        except BaseApiRequestError:
            return False


class IsAppTokenCorrect(BaseAuthPermission):
    def has_permission(self, request, view):
        token = self._get_token_from_request(request)
        if token is None:
            return False
        view.app_access_token = token
        return AuthRequester().app_verify_token(token)[1]

