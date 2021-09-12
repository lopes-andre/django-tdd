from django.test import TestCase
from selenium import webdriver

class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_there_is_homepage(self):
        '''
        Tests the home page for having the text an specific
        text on the page source.
        '''
        self.browser.get('http://localhost:8000')
        self.assertIn('Enter your text to be encoded to a hash:', self.browser.page_source)

    def tearDown(self):
        self.browser.quit()
