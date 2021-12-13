from rest_framework import views, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from core.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostList(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentList(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class UpvotePostAPIView(views.APIView):

    def patch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['id'])
        post.upvote_count += 1
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            post = serializer.save()
            return Response(PostSerializer(post).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
