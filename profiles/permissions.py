from rest_framework.permissions import BasePermission, SAFE_METHODS


class UpdateOwnProfile(BasePermission):
    """ Base Permissions To Update Profile """

    def has_object_permission(self, request, view, obj):
        """ Check If User Is Trying To Update His Profile """
        if request.method in SAFE_METHODS:
            return True

        return obj.id == request.user.id