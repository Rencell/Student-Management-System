
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from my_apps.student.views import StudentViewSet, EnrollmentViewSet
from my_apps.subject.views import SubjectViewSet
from my_apps.grade.views import GradeViewSet
from my_apps.classes.views import ClassesViewSet, ClassesStudentViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'enrollment', EnrollmentViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'classes', ClassesViewSet)
router.register(r'classes_student', ClassesStudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('dj-rest-auth/', include('dj_rest_auth.urls'))
]
