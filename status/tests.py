from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from django.utils import timezone
from .models import StatusModel
from .views import status, about
from .forms import StatusForm

class StatusUnitTest(TestCase):
    def test_status_url_is_exist(self):
        response = Client().get('/status/')
        self.assertEqual(response.status_code, 200)

    def test_status_using_status_func(self):
        found = resolve('/status/')
        self.assertEqual(found.func, status)

    def test_status_template_used(self):
        response = Client().get('/status/')
        self.assertTemplateUsed(response, 'status.html')

    def test_status_object_to_database(self):
        StatusModel.objects.create(content='hai', date=timezone.now())
        count_status = StatusModel.objects.all().count()
        self.assertEqual(count_status, 1)

    def test_form_validated(self):
        form = StatusForm(data={'content':'', 'date':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['your_status'],
            ['This field is required.']
        )

    def test_status_page_is_completed(self):
        test_str = 'hai'
        response_post = Client().post('/status/', {'content': test_str, 'date': timezone.now()})
        self.assertEqual(response_post.status_code, 200)

    def test_about_url_is_exist(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_using_about_func(self):
        found = resolve('/about/')
        self.assertEqual(found.func, about)

    def test_about_template_used(self):
        response = Client().get('/about/')
        self.assertTemplateUsed(response, 'about.html')