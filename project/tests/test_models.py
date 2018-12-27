from django import utils
from django.test import TestCase

from scrapetest_a.models import Response, ScrapeTest


class TestScrapeTestModel(TestCase):

    def setUp(self):
        st = ScrapeTest.objects.create(
                text_to_find='exa',
                url='http://example.com',
                timestamp=utils.timezone.now())

        resp = Response.objects.create(
                search=st,
        loader = 'test',
        status_code = 200,
        text_in_response = True,
        response = 'exammmmm',
        timestamp =utils.timezone.now(),
        error = 'kjkj'
        )

    def test_nothing(self):
        #for setUp work
        pass
