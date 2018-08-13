from django.contrib.auth.mixins import LoginRequiredMixin

from courses.models import Course


class OwnerMixin:

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class OwnerEditMixin:

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid()


class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin):
    model = Course
