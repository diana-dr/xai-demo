from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from xai_backend import tests, views
from xai_backend import services


router = DefaultRouter()
router.register('xai_backend', views.SongViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('getranking', services.sample_ranking),
    path('compareranking', services.compare_rankings),
    # path('userpreference', services.get_user_preference),
    path('shap', services.get_shap),
]