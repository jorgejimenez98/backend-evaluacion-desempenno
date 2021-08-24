from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from backend import utils
from .serializers.userSerializer import UserSerializerWithToken


# AUTHENTICATION PROCESS


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        initialData = self.initial_data
        try:
            user = User.objects.get(username=initialData.get('username'))
            if not user.check_password(initialData.get('password')):
                return Response({'detail': utils.getLoginErrorMessage()}).data
            data = super().validate(attrs)
            serializer = UserSerializerWithToken(self.user).data
            for k, v in serializer.items():
                data[k] = v
            return data
        except User.DoesNotExist:
            return Response({'detail': utils.getUserNotExistMessage(initialData.get('username'))}).data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
