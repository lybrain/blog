from rest_framework import routers
from about.api.views import WishMessageViewSet

wish_message_router = routers.DefaultRouter()
wish_message_router.register('wish_message', WishMessageViewSet, basename='wish-message')
