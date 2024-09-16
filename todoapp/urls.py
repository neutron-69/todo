
from django.contrib import admin
from django.urls import include, path
from todoapp.views import (
    TodoTemplate,
    TodoAddAPI,
    MarkCompleteApi,
    UserLoginApi,
    logintemplaterender,
    logoutApi,
    SignupTemplateRender,
    signupApi,
    DeleteTaskApi,
    RenderEditView,
    UpdateTaskApi
    )

urlpatterns = [
    path("todos/",TodoTemplate.as_view(),name='todo-home'),
    path("todo-add/",TodoAddAPI.as_view(),name='todo-add'),
    path("mark-complete/<int:id>/",MarkCompleteApi.as_view(),name='mark-complete'),
    path("login-api/",UserLoginApi.as_view(),name='login-api'),
    path("login/",logintemplaterender.as_view(),name='login'),
    path("logout/",logoutApi.as_view(),name='logout'),
    path("signup-page/",SignupTemplateRender.as_view(),name='signup-page'),
    path("signupApi/",signupApi.as_view(),name='signup'),
    path("delete-task/<int:id>/",DeleteTaskApi.as_view(),name='delete-task'),
    path("edit-task/<int:id>/",RenderEditView.as_view(),name='edit-task'),
    path("update-task/",UpdateTaskApi.as_view(),name='update-task'),
]