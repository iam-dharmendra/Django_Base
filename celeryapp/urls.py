from django.urls import path
from celeryapp import views
urlpatterns = [
    path('home/',views.HomeView.as_view(),name='home'),
]
