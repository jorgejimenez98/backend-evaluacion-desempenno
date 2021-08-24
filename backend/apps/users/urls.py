# django-rest-framework imports
from rest_framework import routers
# Django imports
from django.urls import path
# Login View
from .views import MyTokenObtainPairView
# View Sets
from .viewSets import userViewSet as userViews
from .viewSets.permissionViewSet import PermissionViewSet

router = routers.DefaultRouter()
# Conjunto de vistas del modelo para mostrarlo en la api
router.register('users', userViews.UserViewSet)
router.register('permissions', PermissionViewSet)

urlpatterns = [
    path('users/login/', MyTokenObtainPairView.as_view(), name='loginView'),
    path('users/profile/update/', userViews.updateUserProfile, name='updateUserProfile'),
    path('users/changePassword/profile/', userViews.updateUserPassword, name='updateUserPassword'),
    path('users/profile/', userViews.getAuthenticatedUserProfile, name='getAuthenticatedUserProfile'),
]
