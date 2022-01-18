from rest_framework import viewsets, status, permissions, mixins
from rest_framework.response import Response
from .models import Post, User
from .serializers import PostSerializer, UserSerializer
import random


# Manual API creation not taking full advantage of Django Rest Framework library
# More control over functionality, takes a bit more time to develop
class Posts(viewsets.ViewSet):

    model = Post
    serializer = PostSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self, **kwargs):
        return self.model.objects.filter(**kwargs)

    def get_object(self, **kwargs):
        return self.get_queryset(id=kwargs.get('id')).first()

    def list(self, request):
        # Return all Posts
        return Response(self.serializer(self.get_queryset().all(), many=True).data)

    def create(self, request):
        serialized = self.serializer(data=request.data)

        if serialized.is_valid(raise_exception=True):
            serialized.save()

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, **kwargs):
        post = self.get_object(**kwargs)

        return Response(self.serializer(post).data)

    def update(self, request, **kwargs):
        post = self.get_object(**kwargs)

        serialized = self.serializer(instance=post, data=request.data, partial=True)

        if serialized.is_valid(raise_exception=True):
            serialized.save()

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, **kwargs):
        post = self.get_object(**kwargs)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# API creation taking advantage of Django Rest Framework library
# So much faster to develop, but takes a bit more effort to override built-in functions
class Users(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    lookup_field = 'id'
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return User.objects

    def list(self, request, *args, **kwargs):
        users = self.get_queryset().all()

        if users:
            user = random.choice(users)
            return Response(self.get_serializer(user).data)

        return Response(data={'error': 'Data not found.'}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        # Modify retrieve function here
        return super().retrieve(self, request, *args, **kwargs)
