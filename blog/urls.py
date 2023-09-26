from django.urls import path
from . import views

urlpatterns = [
    # path('', views.blog_post_list, name='blog_post_list'),
    # path('create/', views.create_blog_post, name='create_blog_post'),
    # path('update/<int:id>', views.update_blog_post, name='update_blog_post'),
    # path('delete/<int:id>', views.delete_blog_post, name='delete_blog_post'),

    # -----------------------urls for class view----------------------
    # pk name  is must for update,delete

    path('', views.BlogListView.as_view(), name='blog_post_list'),
    path('view/<int:pk>', views.BlogDetailView.as_view(), name='view_blog'),
    path('update/<int:pk>', views.BlogUpdateView.as_view(), name='update_blog_post'),
    path('delete/<int:pk>', views.BlogDeleteview.as_view(), name='delete_blog_post'),
    
    path('create', views.BlogCreateView.as_view(), name='create_blog')

    # Define other URL patterns for your views
]