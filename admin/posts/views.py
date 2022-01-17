from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


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
