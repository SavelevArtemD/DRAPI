from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views.mixed_in_generic_views import SnippetList, SnippetDetail
from snippets.views.user_views import UserList, UserDetail

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
