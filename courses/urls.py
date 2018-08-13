from django.urls import path

from courses.views import ManageCourseListView

app_name = 'courses'
urlpatterns = [
    path('list/', ManageCourseListView, name='course_list'),
]
