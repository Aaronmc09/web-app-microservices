from django.urls import path
from .views import Posts

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
]
