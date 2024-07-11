from well.apps import WellConfig
from rest_framework.routers import DefaultRouter

from well.views import WellViewSet

app_name = WellConfig.name


router = DefaultRouter()
router.register("", WellViewSet, basename='well')
urlpatterns = []
urlpatterns += router.urls
