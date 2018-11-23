from django.urls import path
from apps.core.views import StudentViewSet, UniversityViewSet, FacultyViewSet

urlpatterns = [
    path('students/', StudentViewSet.as_view()),
    path('universities/', UniversityViewSet.as_view()),
    path('faculties/', FacultyViewSet.as_view())
]

# router.register(r'students', StudentViewSet)
# router.register(r'universities', UniversityViewSet)
# router.register(r'faculties', FacultyViewSet)

app_name = 'core'

# urlpatterns = router.urls