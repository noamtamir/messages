from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from messagingApp.views import MessageViewSet


router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('api/', include('rest_framework.urls', namespace='rest_framework'))
]