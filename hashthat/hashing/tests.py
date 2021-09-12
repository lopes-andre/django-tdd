from django.test import TestCase
from selenium import webdriver
from .forms import HashForm
from .models import Hash
import hashlib

# class FunctionalTestCase(TestCase):

#     def setUp(self):
#         self.browser = webdriver.Firefox()

#     def test_there_is_homepage(self):
#         '''
#         Tests the home page for having the text an specific
#         text on the page source.
#         '''
#         self.browser.get('http://localhost:8000')
#         self.assertIn('Enter your text to be encoded to a hash:', self.browser.page_source)

#     def test_hash_of_hello(self):
#         '''
#         Tests finding a form text element by its id, filling it
#         with a 'hello' string and submiting it; then asserts for
#         its correspondent hash in the home page source.
#         '''
#         self.browser.get('http://localhost:8000')
#         text = self.browser.find_element_by_id('id_text')
#         text.send_keys('hello')
#         self.browser.find_element_by_name('submit').click()
#         self.assertIn(
#             '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824',
#             self.browser.page_source
#         )

#     def tearDown(self):
#         self.browser.quit()

class UnitTestCase(TestCase):

    def test_home_template(self):
        '''
        Tests if the response to the root URL is being to
        render the proper template.
        '''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hashing/home.html')

    def test_hash_form(self):
        '''
        Tests if the form is being loaded and if passing
        a string to the text area is valid.
        '''
        form = HashForm(data = { 'text': 'hello' })
        self.assertTrue(form.is_valid())

    def test_hash_works(self):
        '''
        Tests if the hashing function is working properly.
        '''
        text_hash = hashlib.sha256('hello'.encode('UTF-8')).hexdigest()
        self.assertEqual(
            '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824',
            text_hash
        )

    def test_hash_object(self):
        '''
        Tests if a given Hash object is being properly saved to the database and
        if when retrieved it matches an specific hash and text.
        '''
        hash = Hash()
        hash.text = 'hello'
        hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        hash.save()
        pulled_hash = Hash.objects.get(text='hello')
        self.assertEqual(hash.hash, pulled_hash.hash)