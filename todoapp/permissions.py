from rest_framework import exceptions, permissions
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect

class IsLoggedIn(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return redirect("todo-home")
        else:
            return redirect("login")