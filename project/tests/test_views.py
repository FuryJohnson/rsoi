import os

import vcr
from django.test import Client
from django.test import TestCase
from rest_framework import status

from config.settings import BASE_DIR
from scrapetest_a.apps import ScrapeMeConfig

APP_NAME = ScrapeMeConfig.name
import requests
import json
client = Client()
SCRAPABLE_URL = 'http://example.com'
NOT_SCRAPABLE_URL = 'https://streeteasy.com/building/32-east-1st-street/4e?featured=1'
INVALID_URL = 'lkjlkj;lkaj.sdf'

scrapable_not_portfolio_item = {
    "text":     "МГТУ",
    "site_url": "http://www.bmstu.ru/",
    "name":     "sf",
    "surname":  "saf",
    "email":    "3r@fdasf.com",
}


class TestScrapetestViews(TestCase):
    my_vcr = vcr.VCR(
            cassette_library_dir=os.path.join(BASE_DIR, APP_NAME, 'tests/cassettes/views')
    )

    @my_vcr.use_cassette()
    def test_valid_url(self):
        response = requests.get(f'http://127.0.0.1:8010/api/v1/scrapetest/?text_to_find=exam&url={SCRAPABLE_URL}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(json.loads(response.content).get('results'))
        for i in json.loads(response.content).get('results'):
            self.assertTrue(i['text_in_response'])
            self.assertIsNone(json.loads(response.content).get(i['error']))

    @my_vcr.use_cassette()
    def test_invalid_url(self):
        response = requests.get(f'http://127.0.0.1:8010/api/v1/scrapetest/?text_to_find=Building&url={INVALID_URL}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for i in json.loads(response.content).get('results'):
            self.assertFalse(i['text_in_response'])

    @my_vcr.use_cassette()
    def test_not_scrapable(self):
        response = requests.get(f'http://127.0.0.1:8010/api/v1/scrapetest/?text_to_find=Building&url={NOT_SCRAPABLE_URL}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(json.loads(response.content).get('results'))
        for i in json.loads(response.content).get('results'):
            self.assertFalse(i['text_in_response'])
    @my_vcr.use_cassette()
    def test_scrapable_by_selenium(self):
        response = requests.get(f'http://127.0.0.1:8010/api/v1/scrapetest/?text_to_find=МГТУ&url=http://www.bmstu.ru/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(json.loads(response.content).get('results'))

        for i in json.loads(response.content).get('results'):
            if i['loader']=='selenium':
                self.assertTrue(i['text_in_response'])
            else:
                self.assertFalse(i['text_in_response'])


