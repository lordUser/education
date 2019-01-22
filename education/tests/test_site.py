from django.test import Client, TestCase
from django.urls import reverse

from students.models import Student, StudentGroup

class TestSite(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.student_create_url = reverse('core:student_create')
        self.student_group = StudentGroup.objects.create(name='Test Group')

    def test_login_POST(self):
        response = self.client.post(self.login_url, {'username': 'tt', 'password': 't'})
        self.assertEqual(response.status_code, 200)

    def test_student_create_POST(self):
        response = self.client.post(self.student_create_url, {'first_name': 'katya', 'fsecond_name': 'polya', 'last_name': 'mila', 'group': self.student_group.id})
        self.assertEqual(response.status_code, 200)
