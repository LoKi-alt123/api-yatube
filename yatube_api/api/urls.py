from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')

comments_list = CommentViewSet.as_view({'get': 'list', 'post': 'create'})
comments_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('api/v1/api-token-auth/', obtain_auth_token),
    path('api/v1/posts/<int:post_id>/comments/', comments_list),
    path('api/v1/posts/<int:post_id>/comments/<int:pk>/', comments_detail),
    path('api/v1/', include(router.urls)),
]