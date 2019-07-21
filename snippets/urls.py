from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets.views import viewsets

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', viewsets.SnippetViewSet)
router.register(r'users', viewsets.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
