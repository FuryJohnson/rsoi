import unittest
from apps.core.views import UniversityViewSet
from apps.core.views import FacultyViewSet


class TestFacultyViewSet(unittest.TestCase):
    def test_create(self):
        rep = FacultyViewSet()
        id1 = rep.create('5bd897f8af13c78fe908cb98', 2)
        id2 = rep.create('5bd897f8af13c78fe908cb98', 2)
        self.assertNotEqual(id1, id2)
        rep.delete(id1)
        rep.delete(id2)

    def test_get_right(self):
        rep = UniversityViewSet()
        faculty_id = rep.create(student_id='5bd897f8af13c78fe908cb98', seat_number=1)
        rep.delete(faculty_id)

    def test_get_error(self):
        rep = FacultyViewSet()
        ticket = rep.get('5bd89fd9')
        self.assertIsNone(ticket)

    def test_read_paginated(self):
        rep = FacultyViewSet()
        tickets = rep.read_paginated(1, 5)
        self.assertLessEqual(len(tickets), 5)

    def test_delete_existed(self):
        rep = FacultyViewSet()
        id1 = rep.create('5bd897f8af13c78fe908cb98', 2)
        rep.delete(id1)
        self.assertFalse(rep.exists(id1))

    def test_exists_true(self):
        rep = FacultyViewSet()
        faculty_id = rep.create(student_id='5bd897f8af13c78fe908cb98', seat_number=1)
        boolean = rep.exists(faculty_id)
        self.assertTrue(boolean)
        rep.delete(faculty_id)

    def test_exists_false(self):
        rep = FacultyViewSet()
        boolean = rep.exists('5bd8ad1daf')
        self.assertFalse(boolean)


if __name__ == '__main__':
    unittest.main()
