from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    message = 'Check is Admin'

    def has_permission(self, request, view):
        return request.user.role == "AD"


class PowerUserPermission(permissions.BasePermission):
    message = 'Check is power user'

    def has_permission(self, request, view):
        return request.user.role == "PU"


class PowerUserOrAdminPermission(permissions.BasePermission):
    message = 'Check is power user or Admin'

    def has_permission(self, request, view):
        return request.user.role == "PU" or "AD"
