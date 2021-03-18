"""Accounts view."""
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import StudentSignUpForm, TeacherSignUpForm
from .models import CustomUser


class StudentSignUpView(CreateView):
    """Sign up view for Student Users."""

    model = CustomUser
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        """Set the `user_type` as "student" in the form data."""
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        """Enable auto login when the form is valid."""
        user = form.save()
        login(self.request, user)
        return redirect('polls:index')


class TeacherSignUpView(CreateView):
    """Sign up view for Teacher Users."""

    model = CustomUser
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        """Set the `user_type` as "student" in the form data."""
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        """Enable auto login when the form is valid."""
        user = form.save()
        login(self.request, user)
        return redirect('polls:index')
