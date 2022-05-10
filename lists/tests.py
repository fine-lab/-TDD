from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class SmokeTest(TestCase):

	def test_root_url_resolve_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		#request = HttpRequest() # 1
		#response = home_page(request) # 2
		response = self.client.get('/') # 1

		html = response.content.decode('utf8') # 2
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do lists</title>', html)
		self.assertTrue(html.endswith('</html>'))

		self.assertTemplateUsed(response, 'home.html') # 3

#	def test_bad_maths(self):
#		self.assertEqual(1 + 1, 3)
		
# Create your tests here.
