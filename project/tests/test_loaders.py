import os
from unittest import TestCase

from config.settings import BASE_DIR
from scrapetest_a.apps import ScrapeMeConfig

APP_NAME = ScrapeMeConfig.name
from scrapetest_a.loaders import by_requests
import vcr
valid_url = 'http://example.com/'
text_from_page = 'exa'
text_not_from_page = 'AAAAAAAAAAAAAAAAAAAAAAAAA'

invalid_url = 'dsaffffffff'

class TestLoader():
    def test_status_code_valid_url(self):
        self.loader.load(valid_url)
        self.assertEqual(self.loader.status_code, 200)

    def test_status_code_invalid_url(self):
        self.loader.load(invalid_url)
        self.assertIsNone(self.loader.status_code)

    def test_response_valid_url(self):
        # valid url
        self.loader.load(valid_url)
        # something there
        self.assertTrue(self.loader.response)

    def test_response_invalid_url(self):
        # valid url
        self.loader.load(invalid_url)
        # something there
        self.assertIsNone(self.loader.response)

    def test_text_in_response_valid_url(self):
        self.loader.load(valid_url)
        self.assertTrue(self.loader.text_in_response(text_from_page))
        self.assertFalse(self.loader.text_in_response(text_not_from_page))

    def test_text_in_response_invalid_url(self):
        self.loader.load(invalid_url)
        self.assertFalse(self.loader.text_in_response(text_from_page))
        self.assertFalse(self.loader.text_in_response(text_not_from_page))

    def test_error_invalid_url(self):
        # something there
        self.loader.load(invalid_url)
        self.assertTrue(self.loader.error)
    def test_error_valid_url(self):
        # something there
        self.loader.load(valid_url)
        self.assertIsNone(self.loader.error)

class TestLoaderRequests(TestCase, TestLoader):
    my_vcr = vcr.VCR(
        cassette_library_dir=os.path.join(BASE_DIR, APP_NAME, 'tests/cassettes/requests')
    )
    @classmethod
    #@my_vcr.use_cassette('valid_url.json')
    def setUpClass(cls):
        cls.loader = by_requests.ByRequestsLoader(valid_url)
    @my_vcr.use_cassette('valid_url.json')
    def test_error_valid_url(self):
        super(TestLoaderRequests, self).test_error_valid_url()
    @my_vcr.use_cassette('valid_url.json')
    def test_response_valid_url(self):
        super(TestLoaderRequests, self).test_response_valid_url()
    @my_vcr.use_cassette('valid_url.json')
    def test_status_code_valid_url(self):
        super(TestLoaderRequests, self).test_status_code_valid_url()
    @my_vcr.use_cassette('valid_url.json')
    def test_text_in_response_valid_url(self):
        super(TestLoaderRequests, self).test_text_in_response_valid_url()


    def test_error_invalid_url(self):
        super(TestLoaderRequests, self).test_error_invalid_url()

    def test_response_invalid_url(self):
        super(TestLoaderRequests, self).test_response_invalid_url()

    def test_status_code_invalid_url(self):
        super(TestLoaderRequests, self).test_status_code_invalid_url()

    def test_text_in_response_invalid_url(self):
        super(TestLoaderRequests, self).test_text_in_response_invalid_url()
        
'''
class TestLoaderSelenium(TestCase, TestLoader):
    my_vcr = vcr.VCR(
        cassette_library_dir='cassetes/selenium')
    @classmethod
    def setUpClass(cls):
        cls.loader = by_selenium.BySeleniumLoader(valid_url)
    @classmethod
    def tearDownClass(cls):
        cls.loader.__exit__()
'''