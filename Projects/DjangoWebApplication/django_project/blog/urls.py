from django.urls import path
from . import views
# url path to home page for the blog
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
