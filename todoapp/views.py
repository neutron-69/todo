from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from todoapp.mixins import IsLoggedInMixin
from .models import Todo
from todoapp.serializers import TodoSerializer
from rest_framework.generics import *
from django.views.generic import TemplateView
from django_filters.views import FilterView
from todoapp.tables import TodoTable
from django_tables2.export.views import ExportMixin
from django_tables2 import SingleTableMixin
from todoapp.permissions import IsLoggedIn
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render

class logoutApi(APIView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")

class logintemplaterender(TemplateView):
    template_name = "login.html"

class UserLoginApi(APIView):
    def post(self,request,*args,**kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return Response({"message":"login successful"},status=status.HTTP_200_OK)
        else:
            return Response({"message":"login failed"},status=status.HTTP_400_BAD_REQUEST)

class SignupTemplateRender(TemplateView):
    template_name = "signup.html"

class signupApi(APIView):
    def post(self,request,*args,**kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        confirm_password = request.POST["confirm_password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        print(username,password,email,confirm_password)
        if(password == confirm_password):
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                    )
                user.save()
                return Response({"message":"signup successful"},status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"message":f"error: {e}"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"passwords do not match"},status=status.HTTP_400_BAD_REQUEST)

class TodoTemplate(IsLoggedInMixin,SingleTableMixin,ExportMixin,FilterView):
    model = Todo
    table_class = TodoTable
    template_name = "todo-template.html"
    export_formats = ["csv"]
    export_name = "Todo List"
    def get_queryset(self):
        return super().get_queryset().filter(auth_user = self.request.user).order_by("duedate")
    
class TodoAddAPI(APIView):
    permission_classes = [IsLoggedIn]
    def post(self,request,*args,**kwargs):
        
        title = request.data.get("title")
        description = request.data.get("description")
        due_date = request.data.get("due_date")
        try:
            new_todo = Todo.objects.create(auth_user = self.request.user,title=title,description=description,duedate=due_date)
            new_todo.save()
            return Response({"message":"task added successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"message":e},status=status.HTTP_400_BAD_REQUEST)


class MarkCompleteApi(APIView):
    permission_classes = [IsLoggedIn]
    def get(self,request,*args,**kwargs):
        try:
            todoitem = Todo.objects.filter(id=self.kwargs["id"]).first()
            if(todoitem.is_completed):
                todoitem.is_completed = False
            else:
                todoitem.is_completed = True
            todoitem.save()
            return redirect("todo-home")
        except Exception as e:
            return Response(data={"message":e},status=status.HTTP_400_BAD_REQUEST)

class DeleteTaskApi(APIView):
    permission_classes = [IsLoggedIn]
    def delete(self,request,*args,**kwargs):
        try:
            todoitem = Todo.objects.filter(id = self.kwargs["id"]).first()
            try:
                todoitem.delete()
                return Response(data={"message":"Error deleting the task"},status=status.HTTP_200_OK)
            except Exception as e:  
                return Response(data={"message":"Error deleting the task"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={"message":e},status=status.HTTP_400_BAD_REQUEST)
        

class EditTemplateApi(IsLoggedInMixin,TemplateView):
    template_name = "edit-todo.html"


class EditTodoApi(APIView):
    permission_classes = [IsLoggedIn]
    def post(self,request,*args,**kwargs):
        try:
            todoitem = Todo.objects.filter(id=self.kwargs["id"]).first()
            todoitem.title = request.data.get("title")
            todoitem.description = request.data.get("description")
            todoitem.duedate = request.data.get("due_date")
            todoitem.save()
            return Response({"message":"task updated successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"message":e},status=status.HTTP_400_BAD_REQUEST)       

class RenderEditView(APIView):
    def get(self,request,*args,**kwargs):
        todoitem = Todo.objects.filter(id=self.kwargs["id"]).first()
        return render(request,"edit_todo.html",context={"todoitem":todoitem})

class UpdateTaskApi(APIView):
    permission_classes = [IsLoggedIn]
    def post(self,request,*args,**kwargs):
        try:
            todoitem = Todo.objects.filter(id=self.kwargs["id"]).first()
            todoitem.title = request.data.get("title")
            todoitem.description = request.data.get("description")
            todoitem.duedate = request.data.get("due_date")
            todoitem.save()
            return Response({"message":"task updated successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"message":e},status=status.HTTP_400_BAD_REQUEST)
        
class UpdateTaskApi(APIView):
    def put(self,request,*args,**kwargs):
        try:
            id=request.data.get("id")
            todoitem = Todo.objects.filter(id=id).first()
            todoitem.title = request.data.get("title")
            todoitem.description = request.data.get("description")
            todoitem.duedate = request.data.get("due_date")
            todoitem.save()
            return Response({"message":"task updated successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"message":e},status=status.HTTP_400_BAD_REQUEST)