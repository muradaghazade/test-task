from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostList, CommentList, UpvotePostAPIView

app_name = 'news'

router = DefaultRouter()
router.register('posts', PostList, basename='post')
router.register('comments', CommentList, basename='comment')
# urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
    path('upvote/<int:id>/', UpvotePostAPIView.as_view(), name='upvote'),
]
