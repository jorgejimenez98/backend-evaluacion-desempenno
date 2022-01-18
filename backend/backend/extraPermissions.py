from rest_framework.permissions import BasePermission


class IsFoodAndDrinkBoss(BasePermission):
    """
    Allows access only to Food And Drink Boss users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.isFoodAndDrinkBoss)
