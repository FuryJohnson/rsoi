from django.conf.urls import url
from rest_framework import routers
from apps.core.views import StudentViewSet, UniversityViewSet, FacultyViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)
router.register(r'faculties', FacultyViewSet)

app_name = 'core'

urlpatterns = router.urls