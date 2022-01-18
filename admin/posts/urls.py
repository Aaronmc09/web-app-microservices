from django.urls import path, include
from rest_framework import routers
from .views import Posts, Users

user_router = routers.SimpleRouter(trailing_slash=False)
user_router.register('', Users, basename='users')

urlpatterns = [
    path('posts', Posts.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('posts/<int:id>', Posts.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('users', include(user_router.urls)),
    path('users/', include(user_router.urls))
]
