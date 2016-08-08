from django.test import TestCase
from django.core.urlresolvers import resolve
from website.views import homepage

# Create your tests here.
class UnitTest(TestCase):
    
    def test_root_url_resolves_to_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_homepage_template_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage.html')
        
