from celery import shared_task
from .models import Post

@shared_task
def reset_upvotes():
    posts = Post.objects.all()
    for post in posts:
        post.upvote_count = 0
        post.save()
