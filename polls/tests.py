from django.test import TestCase

# Create your tests here.
from django.utils.timezone import now
from .models import Question, Choice
from datetime import timedelta
from django.urls import reverse
from django.test import Client
from parameterized import parameterized


class QuestionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Question.objects.create(question_text='test question', pub_date=now())

    def test_question_text_field_value(self):
        question = Question.objects.create(question_text='Question 1',
                                           pub_date=now())
        self.assertEqual('Question 1', question.question_text)

    @parameterized.expand([
        (now() + timedelta(days=30), False),
        (now() - timedelta(days=1, seconds=1), False),
        (now() - timedelta(hours=23, minutes=59, seconds=59), True),
    ])
    def test_was_published_recently(self, input, expected):
        question = Question(pub_date=input)
        self.assertEqual(question.was_published_recently(), expected)


class ChoiceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        question = Question.objects.create(question_text='test question',
                                           pub_date=now())
        Choice.objects.create(question=question, choice_text="choice 1")
        Choice.objects.create(question=question, choice_text="choice 2",
                              votes=3000)

    def test_choice_test_field_value(self):
        choice = Choice.objects.get(id=1)
        self.assertEqual('choice 1', choice.choice_text)

    def test_choice_votes_value(self):
        choice1 = Choice.objects.get(id=1)
        choice2 = Choice.objects.get(id=2)
        self.assertEqual(0, choice1.votes)
        self.assertEqual(3000, choice2.votes)


class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
