from django.test import TestCase
from django.urls import reverse

class HomepageTest(TestCase):
    def testhomepagename(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    #
    def testHomepage_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'homepage')
    def test_homepage_template_content(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


