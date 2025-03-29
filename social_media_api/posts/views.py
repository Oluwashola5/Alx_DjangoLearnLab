from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Like, Post
from .serializers import LikeSerializer
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer

class LikePostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # Ensure this is included
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)

class UnlikePostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # Ensure this is included
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
            return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)

        return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)


class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({"message": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification
        Notification.objects.create(
            recipient=post.user,
            actor=request.user,
            verb="liked your post",
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )

        return Response({"message": "Liked"}, status=status.HTTP_201_CREATED)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            like = Like.objects.get(user=request.user, post_id=pk)
            like.delete()
            return Response({"message": "Unliked"}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"message": "Not liked"}, status=status.HTTP_400_BAD_REQUEST)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()  # Explicitly include this
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_pk')
        if post_id:
            return Comment.objects.filter(post_id=post_id).order_by('-created_at')
        return Comment.objects.all()  # Ensure it returns all comments when no post_id is provided

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
