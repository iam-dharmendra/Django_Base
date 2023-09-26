from typing import Any
from django import http
from django.views.generic import TemplateView,RedirectView,ListView,DeleteView,UpdateView,CreateView,DetailView,View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .form import RegisterForm,LoginForm
from django.contrib.auth import login
from django.contrib.auth.models import Group
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            """ here we add a user into a group (for now assume that group already created from django admin panel )"""
            # g=Group.objects.get(name='editor')
            # user.groups.add(g)
            
            return redirect('login')  # Redirect to a suitable page after registration
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


class Registerview(CreateView):
    # form_class=UserCreationForm
    form_class=RegisterForm
    template_name='registration/register.html'
    success_url='/user/login'     



from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    next_page='blog_post_list' 
    # (either set here or set in setting.py to where redirect after logout)


""" another method to login """

# def user_login(request):
#     template_name = 'registration/login.html'
#     if request.method=='POST':
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             user=form.cleaned_data['user']
#             login(request,user)
#             return redirect('/blog')
#     form=LoginForm()
#     context={
#         'form':form
#     }
#     return render(request,template_name,context)

class CustomLogoutView(LogoutView):
    next_page = 'login' 
    # (either set here or set in setting.py to where redirect after logout)
    pass
    # logout(request)

    # or 
# we can use inboult logout function








""" Class based drf API"""

from rest_framework.views import APIView
from .serializer import RegisterSerializer,UpdateUserApi
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework import pagination

""" most used it"""
class QueryserApi():

    def get_object(self,model,pk=None):

        if pk:
            return model.objects.get(pk=pk)
        return model.objects.all()
        


class RegisterApiView(APIView,QueryserApi):

    serializer_class=RegisterSerializer

    # def get_queryset(self):
    #     return User.objects.all()

    def get(self,request):

        obj=self.get_object(User)
        serializer=self.serializer_class(obj,many=True)
        return Response({'msg':'data get successfully','data':serializer.data},status=status.HTTP_200_OK)


    def post(self,request):

        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data saved successfully','data':serializer.data},status=status.HTTP_200_OK)
        
        return Response({'msg':'some error occur','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteApi(APIView,QueryserApi):

    serilaizer_class=UpdateUserApi

    def put(self,request,pk):
        obj=self.get_object(User,pk=pk)
        serializer=self.serilaizer_class(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data saved successfully','data':serializer.data},status=status.HTTP_200_OK)
        
        return Response({'msg':'some error occur','data':serializer.errors},status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self,request,pk):
        obj=self.get_object(User,pk=pk)
        obj.delete()
        return Response({'msg':'data saved successfully','data':''},status=status.HTTP_200_OK)
        


""" drf api using genrics api and mixin  not so much used """

# list and create
# class LCUserApi(GenericAPIView,ListModelMixin,CreateModelMixin):

#     queryset=User.objects.all()
#     serializer_class=RegisterSerializer
    

#     # to override use get_querset (user.objects.filter(name='joe')) either write queryset or this method not both together 
#     # def get_queryset(self):
#     #     return super().get_queryset()

#     def get(self,request,*args,**kwargs):
#         return self.list(self,request,*args,**kwargs)

    
#     def post(self,request,*args,**kwargs):
#         return self.create(self,request,*args,**kwargs)    



# # singleobject retrive ,update,delete
# class RUDUserApi(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):

#     queryset=User.objects.all()
#     serializer_class=RegisterSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(self,request,*args,**kwargs)

    
#     def put(self,request,*args,**kwargs):
#         return self.update(self,request,*args,**kwargs)    

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(self,request,*args,**kwargs)
    








""" drf api using genrics api and mixin  not so much used """

#     # to override queryset use get_querset (user.objects.filter(name='joe')) either write queryset or this method not both together

# list and create
# class LCUserApi(ListCreateAPIView):

#     # queryset=User.objects.all()
#     serializer_class=RegisterSerializer


#     # def list(self, request):
#     #     # Note the use of `get_queryset()` instead of `self.queryset`
#     #     queryset = self.get_queryset()
#     #     serializer = UserSerializer(queryset, many=True)
#     #     return Response(serializer.data)
    
#     # def create(self, request, *args, **kwargs):
#     #     return super().create(request, *args, **kwargs)

#     def get_queryset(self):
#         return User.objects.filter(first_name='user5')

# singleobject retrive ,update,delete
# class RUDUserApi(RetrieveUpdateDestroyAPIView):

#     queryset=User.objects.all()
#     serializer_class=UpdateUserApi
    


""" drf api using view most used it """



class Allcrudviewset(viewsets.ViewSet,QueryserApi):

    
    def list(self,request):
        obj=self.get_object(User)
        serializer=RegisterSerializer(obj,many=True)
        return Response({'msg':'success full','data':serializer.data},status=status.HTTP_200_OK)
        
    
    def create(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'success full','data':serializer.data},status=status.HTTP_200_OK)
        
        return Response({'msg':'not success full','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        obj=self.get_object(User,pk=pk)
        serializer=RegisterSerializer(obj)
        return Response({'msg':'success full','data':serializer.data},status=status.HTTP_200_OK)
        

    def partial_update(self,request,pk=None):
        obj=self.get_object(User,pk=pk)
        serializer=UpdateUserApi(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'success full','data':serializer.data},status=status.HTTP_200_OK)
        
        return Response({'msg':'not success full','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self,request,pk=None):
        obj=self.get_object(User,pk=pk)
        obj.delete()
        return Response({'msg':'success full'},status=status.HTTP_200_OK)
        
