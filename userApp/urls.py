from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('allapi',views.Allcrudviewset,basename='allapi')


urlpatterns = [
    # path('register/', views.register, name='register'),
    
    # --------------------for class based register
    path('register/', views.Registerview.as_view(), name='register'),
    
    path('login/', views.CustomLoginView.as_view(), name='login'),
    # path('login/', views.user_login, name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),


    # ---- Drf Api----------#

    # path('registerapi/',views.RegisterApiView.as_view(),name='registerapi'),
    # path('updateapi/<int:pk>/',views.UpdateDeleteApi.as_view(),name='updateapi'),

    
    # # ---- genrics and mixin  based Api not so much used ----------#
    # path('registerapi/',views.LCUserApi.as_view(),name='registerapi'),
    # path('updateapi/<int:pk>/',views.RUDUserApi.as_view(),name='updateapi')

    
    # # ---- genrics ased Api not so much used ----------#
    # path('registerapi/',views.LCUserApi.as_view(),name='registerapi'),
    # path('updateapi/<int:pk>/',views.RUDUserApi.as_view(),name='updateapi')

    # """ most used """

    path('',include(router.urls))

    
]
