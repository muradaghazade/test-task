from django.db import models

class Post(models.Model):
    title = models.CharField('Title',max_length=50)
    link = models.CharField('Link',max_length=150)
    author_name = models.CharField('Author name',max_length=50)
    upvote_count = models.IntegerField('Upvote count',default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    author_name = models.CharField('Author name',max_length=50, null=True)
    content = models.TextField('Content')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, db_index=True, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"{self.content}"
