from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from .views import greeting_view

# Create your tests here.


class TestGreetingView(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser', password='test')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_greeting_not_auth(self):
        request = self.factory.get('/test/greeting')
        request.user = AnonymousUser()
        response = greeting_view(request)
        self.assertEquals(response.status_code, 302)

    def test_user_auth(self):
        request = self.factory.get('/test/greeting')
        request.user = self.test_user
        response = greeting_view(request)
        self.assertEquals(response.status_code, 200)
