import requests
from config import current_config
import unittest

class TestUniversityViewSet(unittest.TestCase):
    def test_post(self):
        payload = {'student_id': '5bd897f8af13c78fe908cb98', 'seat_number': 2}
        res = requests.post(current_config.TICKET_SERVICE_URL + current_config.TICKET_SERVICE_PATH +
                            current_config.CREATE_PATH, data=jsonpickle.encode(payload))
        self.assertEqual(res.status_code, 201)
        ticket = Ticket.from_json(res.content)
        requests.delete(current_config.TICKET_SERVICE_URL + current_config.TICKET_SERVICE_PATH +
                        "/%s" % str(ticket.id))


class TestFacultyViewSet(unittest.TestCase):
    def test_get_right(self):
        res = requests.get(current_config.TICKET_SERVICE_URL + current_config.TICKET_SERVICE_PATH +
                           "/5bd89fd9af13c7ea848cb9dc")
        self.assertEqual(res.status_code, 200)

    def test_get_error(self):
        res = requests.get(current_config.TICKET_SERVICE_URL + current_config.TICKET_SERVICE_PATH +
                           "/5bd0a351")
        self.assertEqual(res.status_code, 404)

    def test_delete_right(self):
        payload = {'student_id': '5bd897f8af13c78fe908cb98', 'seat_number': 2}
        res = requests.post(current_config.TICKET_SERVICE_URL + current_config.TICKET_SERVICE_PATH +
                            current_config.CREATE_PATH, data=jsonpickle.encode(payload))
        ticket = Ticket.from_json(res.content)
        res = requests.delete(current_config.TICKET_SERVICE_URL + current_config.TICKET_SERVICE_PATH +
                              "/%s" % ticket.id)
        self.assertEqual(res.status_code, 204)


class TestTicketListResource(unittest.TestCase):
    def test_get(self):
        payload = (('page', 1), ('page_size', 5))
        res = requests.get(current_config.TICKET_SERVICE_URL + current_config.TICKET_SERVICE_PATH, params=payload)
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
