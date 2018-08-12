from django.views.generic import ListView

from courses.models import Course


class ManageCourseListView(ListView):
    model = Course
    template_name = 'courses/manage/course/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)