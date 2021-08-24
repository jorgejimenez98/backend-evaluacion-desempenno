from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from ..serializers.permissionSerializer import PermissionSerializer, Permission


class PermissionViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
