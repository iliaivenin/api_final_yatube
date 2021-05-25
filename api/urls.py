from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register(
    'posts',
    PostViewSet,
    basename='posts')
router_v1.register(
    'group',
    GroupViewSet,
    basename='group')
router_v1.register(
    'follow',
    FollowViewSet,
    basename='follow')


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router_v1.urls)),
]
