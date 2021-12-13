from rest_framework import serializers
from core.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author_name', 'content', 'post', 'created_at')


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'author_name', 'upvote_count', 'created_at', 'comments')
