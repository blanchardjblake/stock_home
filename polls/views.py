"""Polls app views."""
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView

# Local imports
from .models import Choice, Question
from users.decorators import teacher_required, student_required


@method_decorator([teacher_required], name='dispatch')
class CreateQuestionView(CreateView):
    """View to create question."""

    model = Question
    fields = ['question_text']
    template_name = 'polls/create_polls.html'
    success_url = reverse_lazy('polls:index')

    def form_valid(self, form):
        """For valid form submission."""
        form.instance.pub_date = now()
        return super().form_valid(form)


@method_decorator([teacher_required], name='dispatch')
class CreateChoiceView(CreateView):
    """View to create choice."""

    model = Choice
    fields = ['choice_text']
    template_name = 'polls/create_choice.html'

    def get_success_url(self):
        """Overwrite the `success_url`."""
        question_id = self.kwargs['pk']
        return reverse_lazy('polls:detail', kwargs={'pk': question_id})

    def form_valid(self, form):
        """If the form data is valid, add current time as `pub_date`."""
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)


class IndexView(generic.ListView):
    """Index view of polls app."""

    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """Detail view of polls app."""

    model = Question
    template_name = 'polls/details.html'


class ResultsView(generic.DetailView):
    """Results view of polls app."""

    model = Question
    template_name = 'polls/results.html'


@student_required
def vote(request, question_id):
    """Vote counter function."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',
                                    args=(question.id,)))
