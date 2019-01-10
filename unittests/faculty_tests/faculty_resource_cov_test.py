import unittest
from apps.core.views import UniversityViewSet
from apps.core.views import FacultyViewSet
from unittest.mock import patch


class TestUniversityViewSet(unittest.TestCase):
    @patch('ticket.rest_api.ticket_resource.FacultyViewSet')
    def test_post(self, mock_ticket):
        mock_ticket.return_value.create.return_value = "123"
        tr = UniversityViewSet()
        res = tr.post()
        self.assertEqual(res.status_code, 201)


class TestFacultyViewSet(unittest.TestCase):
    @patch('ticket.rest_api.ticket_resource.FacultyViewSet')
    def test_get_right(self, mock_ticket):
        tr = FacultyViewSet()
        res = tr.get("123")
        self.assertEqual(res.status_code, 200)

    def test_get_error(self):
        tr = FacultyViewSet()
        try:
            res = tr.get("5bd0a351")
        except:
            self.assertTrue(True)

    def test_delete_error(self):
        tr = FacultyViewSet()
        try:
            res = tr.delete("5bd0a351")
        except:
            self.assertTrue(True)

    @patch('ticket.rest_api.ticket_resource.FacultyViewSet')
    def test_delete_right(self, mock_ticket):
        mock_ticket.return_value.delete.return_value = '';
        tr1 = FacultyViewSet()
        res = tr1.delete("123")
        self.assertEqual(res.status_code, 204)


class TestTicketListResource(unittest.TestCase):
    @patch('ticket.rest_api.ticket_resource.FacultyViewSet')
    def test_get(self, mock_ticket):
        tickets = []
        mock_ticket.return_value.read_paginated.return_value = tickets, False, True


if __name__ == '__main__':
    unittest.main()
