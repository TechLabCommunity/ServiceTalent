from django.test import TestCase
from django.http import response

# Create your tests here.

def test_about_us_page_works(self):
    response = self.client.get("/ticketing/homepage/")
    self.assertEqual(response.status_code,200)
    self.assertTemplateUsed(response, 'homepage.html')
    self.assertContains(response, 'ticketing')
    