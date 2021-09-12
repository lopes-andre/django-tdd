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

    def test_hash_of_hello(self):
        '''
        Tests finding a form text element by its id, filling it
        with a 'hello' string and submiting it; then asserts for
        its correspondent hash in the home page source.
        '''
        self.browser.get('http://localhost:8000')
        text = self.browser.find_element_by_id('id_text')
        text.send_keys('hello')
        self.browser.find_element_by_name('submit').click()
        self.assertIn(
            '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824',
            self.browser.page_source
        )

    def tearDown(self):
        self.browser.quit()
