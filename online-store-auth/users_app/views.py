from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView, Response, Request
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from users_app.serializers import RegisterSerializer, UserSerializer, ChangePasswordSerializer


class RegisterView(APIView):
    def post(self, request: Request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token = RefreshToken.for_user(serializer.instance)
            token['username'] = serializer.instance.username
            data = {
                'refresh': str(token),
                'access': str(token.access_token),
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInfoView(APIView):
    def get(self, request):
        print(request.user)
        serializer = UserSerializer(instance=request.user)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserListView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UserDetailView(APIView):

    def get(self, request: Request, pk: int):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePasswordView(APIView):
    def patch(self, request: Request):
        user = request.user
        s = ChangePasswordSerializer(data=request.data, instance=user)
        if s.is_valid():
            s.save()
            token = RefreshToken.for_user(request.user)
            token['username'] = request.user.username
            data = {
                'refresh': str(token),
                'access': str(token.access_token),
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)