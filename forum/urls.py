from django.urls import path
from .views import index, user_login, PostListView, PostCreateView

urlpatterns = [
    path('', user_login, name='login'), 
    path('index/', index, name='index'),
    path('create/', PostCreateView.as_view(), name='post_create'),
]