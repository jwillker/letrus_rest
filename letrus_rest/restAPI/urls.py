# rerouting all requests that have ‘api’ in the url to the <code>apps.core.urls
from django.conf.urls import url
from rest_framework import routers
from letrus_rest.restAPI.views import StudentViewSet, UniversityViewSet, CustomView
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'customview', CustomView.as_view()),
    url(r'^docs/', schema_view),
]
 
urlpatterns += router.urls