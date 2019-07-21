from django.urls import path, include
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views.mixed_in_generic_views import SnippetList, SnippetDetail, api_root, SnippetHighlight
from snippets.views.user_views import UserList, UserDetail
from snippets.views.viewsets import SnippetViewSet, UserViewSet

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])

# _____________________________________________
# patterns with generic class-based views
# ---------------------------------------------
# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('snippets/',
#          SnippetList.as_view(),
#          name='snippet-list'),
#     path('snippets/<int:pk>/',
#          SnippetDetail.as_view(),
#          name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/',
#          SnippetHighlight.as_view(),
#          name='snippet-highlight'),
#     path('users/',
#          UserList.as_view(),
#          name='user-list'),
#     path('users/<int:pk>/',
#          UserDetail.as_view(),
#          name='user-detail')
# ])

# urlpatterns = format_suffix_patterns(urlpatterns)
