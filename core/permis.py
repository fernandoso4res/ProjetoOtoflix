from rest_framework import permissions


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.user == is_student:
            return False
        return False
