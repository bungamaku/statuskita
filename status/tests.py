from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from django.utils import timezone
from .models import Status
from .views import index
from .forms import StatusForm

class StatusUnitTest(TestCase):
def test_status_url_is_exist(self):
    response = Client().get('/status/')
    self.assertEqual(response.status_code, 200)

def test_status_using_index_func(self):
    found = resolve('/status/')
    self.assertEqual(found.func, index)

def test_index_template_used(self):
    response = Client().get('/status/')
    self.assertTemplateUsed(response, 'index.html')

def test_status_object_to_database(self):
    Status.objects.create(content='hai', date=timezone.now())
    count_status = Status.objects.all().count()
    self.assertEqual(count_status, 1)

def test_form_validated(self):
    form = StatusForm(data={'content':'', 'date':''})
    self.assertFalse(form.is_valid())
    self.assertEqual(
        form.errors['content'],
        ['Status is required']
    )

def test_status_content_is_written(self):
    self.assertIsNotNone(status_content)
    self.assertTrue(len(status_content) >= 300)

def test_status_page_is_completed(self):
    response_post = Client().post('/status/', {'content':'hai', 'date': timezone.now()})
    self.assertEqual(response_post.status_code, 302)
    response = Client().get('/status/')
    html_response = response.content.decode('utf8')
    for status in all_status:
    self.assertIn(status, html_response)