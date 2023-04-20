from django.urls import include, path
from rest_framework import routers
from candidates.api.viewsets import CandidatesViewSet, ReportViewSet


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'candidates', CandidatesViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('report/', ReportViewSet.as_view(), name="report"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]