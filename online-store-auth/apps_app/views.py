from rest_framework import status
from rest_framework.views import Response, Request, APIView
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework_simplejwt.state import token_backend
from rest_framework_simplejwt.exceptions import TokenBackendError
from jwt.exceptions import InvalidTokenError
from apps_app.models import App
from apps_app.serializers import AppSerializer, TokenForAppSerializer
from apps_app.token import AppRefreshToken


class AppsView(ListCreateAPIView):
    serializer_class = AppSerializer

    def get_queryset(self):
        return App.objects.all()

    def post(self, request: Request, *args, **kwargs):
        serialized = AppSerializer(data=request.data)
        if serialized.is_valid():
            app = serialized.save()
            token = AppRefreshToken.for_user(app)
            data = {
                'refresh': str(token),
                'access': str(token.access_token),
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class AppView(RetrieveDestroyAPIView):
    serializer_class = AppSerializer

    def get_queryset(self):
        return App.objects.all()


class GetTokenPairForApp(APIView):

    def post(self, request: Request):
        serialized = TokenForAppSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            app = App.objects.get(id=serialized['id'].value, secret=serialized['secret'].value, is_internal=True)
        except App.DoesNotExist:
            return Response({'error': 'Wrong app credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        token = AppRefreshToken.for_user(app)
        data = {
            'access': str(token.access_token),
            'refresh': str(token),
        }
        return Response(data, status=status.HTTP_200_OK)


class VerifyTokenForApp(APIView):
    def post(self, request: Request):
        try:
            token = request.data['token']
        except KeyError:
            return Response({'error': 'Field "token" is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            payload = token_backend.decode(token)
        except (InvalidTokenError, TokenBackendError):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            token_type = payload['token_type']
        except KeyError:
            return Response({'error': 'No token_type for token was given'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            app_id = payload['id']
        except KeyError:
            return Response({'error', 'No id in token'}, status=status.HTTP_401_UNAUTHORIZED)
        if token_type != AppRefreshToken().access_token.token_type:
            return Response({'error': 'Wrong token_type'}, status=status.HTTP_401_UNAUTHORIZED)

        # Exp_time проверяется в decode
        if App.objects.filter(id=app_id).exists():
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RefreshTokenForApp(APIView):
    def post(self, request: Request):
        try:
            token = request.data['refresh']
        except KeyError:
            return Response({'error': 'Field "refresh" is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            payload = token_backend.decode(token)
        except (InvalidTokenError, TokenBackendError):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            token_type = payload['token_type']
        except KeyError:
            return Response({'error': 'No token_type for token was given'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            app_id = payload['id']
        except KeyError:
            return Response({'error', 'No id in token'}, status=status.HTTP_401_UNAUTHORIZED)
        if token_type != AppRefreshToken.token_type:
            return Response({'error': 'Wrong token_type'}, status=status.HTTP_401_UNAUTHORIZED)

        if not App.objects.filter(id=app_id).exists():
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        refresh = AppRefreshToken(token=token, verify=False)
        data = {
            'access': str(refresh.access_token),
        }
        return Response(data, status=status.HTTP_200_OK)