from rest_framework import routers

from .views import GhostintheshellViewSet

router = routers.DefaultRouter()
router.register(r'ghostintheshells', GhostintheshellViewSet)
