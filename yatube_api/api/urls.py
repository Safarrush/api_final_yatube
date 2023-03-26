from django.urls import path, include
from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('group', GroupViewSet, basename='group')
router.register('follow', FollowViewSet, basename='followers')
router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment',
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
