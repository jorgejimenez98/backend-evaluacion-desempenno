from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Permission
from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from backend import utils
from ..serializers.userSerializer import UserSerializer, UserMiniSerializer, User, UserSerializerWithToken


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('pk')
    serializer_class = UserMiniSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        return Response(UserSerializer(self.get_object(), many=False).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def deleteUsers(self, request):
        try:
            for user in request.data:
                User.objects.get(pk=user.get('id')).delete()
            return Response({'Users Eliminated Successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['PUT'])
    def changePassword(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            user.password = make_password(request.data.get('password'))
            user.save()
            return Response({'Password Changed Successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            user = User.objects.create(
                username=data.get('username'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email'),
                is_staff=data.get('isAdmin'),
                password=make_password(data.get('password'))
            )
            if data.get('isFoodAndDrinkBoss'):
                permission = Permission.objects.get(codename='isFoodAndDrinkBoss')
                user.user_permissions.add(permission)
            user.save()
            return Response({'Users Created Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            message = 'Ya existe un usuario con el nombre de usuario {}'.format(data['username'])
            return Response({'detail': message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        data = request.data
        user = User.objects.get(pk=self.get_object().pk)
        try:
            if user.is_staff and not data.get('isAdmin') and User.objects.filter(is_staff=True).count() == 1:
                raise Exception(utils.getNoAdminDeleteMessage(user.username))
            user.username = data.get('username')
            user.first_name = data.get('first_name')
            user.last_name = data.get('last_name')
            user.email = data.get('email')
            user.is_staff = data.get('isAdmin')
            permission = Permission.objects.get(codename='isFoodAndDrinkBoss')
            if not user.user_permissions.filter(codename='isFoodAndDrinkBoss').exists():
                if data.get('isFoodAndDrinkBoss'):
                    user.user_permissions.add(permission)
            elif not data.get('isFoodAndDrinkBoss'):
                user.user_permissions.remove(permission)
            user.save()
            return Response({'Users Edited Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            message = 'Ya existe un usuario con el nombre de usuario {}'.format(data['username'])
            return Response({'detail': message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


""" Authenticated User Views, thats the reason for the functional Views and is not inside the Class ViewSet"""


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAuthenticatedUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False).data
    return Response(serializer)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    data = request.data
    try:
        user.username = data.get('username')
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.email = data.get('email')
        user.save()
        return Response(UserSerializerWithToken(user, many=False).data, status=status.HTTP_200_OK)
    except IntegrityError:
        message = 'Ya existe un usuario con el nombre de usuario {}'.format(data['username'])
        return Response({'detail': message}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserPassword(request):
    user = request.user
    data = request.data
    try:
        if not user.check_password(data.get('oldPassword')):
            raise Exception('La actual contraseña no es correcta, inténtelo de nuevo')
        user.password = make_password(data.get('newPassword'))
        user.save()
        return Response(UserSerializerWithToken(user, many=False).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
