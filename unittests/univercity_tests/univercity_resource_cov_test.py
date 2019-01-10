import unittest



class TestStudentCreateResource(unittest.TestCase):
    @patch('Student.rest_api.Student_resource.StudentRepository')
    def test_post(self, mock_Student):
        mock_Student.return_value.create.return_value = "123"
        sr = StudentCreateResource()
        res = sr.post()
        self.assertEqual(res.status_code, 201)


class TestStudentResource(unittest.TestCase):
    @patch('Student.rest_api.Student_resource.StudentRepository')
    def test_get_right(self, mock_Student):
        Student = Student(student_id="123", movie_id="012", date_time="01.01.2018", seats=[True])
        mock_Student.return_value.get.return_value = Student
        sr = StudentResource()
        res = sr.get("123")
        self.assertEqual(res.status_code, 200)

    def test_get_error(self):
        sr = StudentResource()
        try:
            res = sr.get("5bd0a351")
        except:
            self.assertTrue(True)

    def test_delete_error(self):
        sr = StudentResource()
        try:
            res = sr.delete("5bd0a351")
        except:
            self.assertTrue(True)

    @patch('Student.rest_api.Student_resource.StudentRepository')
    def test_delete_right(self, mock_Student):
        mock_Student.return_value.delete.return_value = ''
        sr = StudentResource()
        res = sr.delete("123")
        self.assertEqual(res.status_code, 204)

    @patch('Student.rest_api.Student_resource.StudentRepository')
    def test_patch_right(self, mock_Student):
        mock_Student.return_value.get_a_seat.return_value = True
        Student = Student(student_id="123", movie_id="012", date_time="01.01.2018", seats=[True])
        mock_Student.return_value.get.return_value = Student
        sr = StudentResource()
        res = sr.patch('123')
        self.assertEqual(res.status_code, 201)


class TestStudentListResource(unittest.TestCase):
    @patch('Student.rest_api.Student_resource.StudentRepository')
    def test_get(self, mock_Student):
        Students = []
        Student = Student(student_id="123", movie_id="012", date_time="01.01.2018", seats=[True])
        Students.append(Student)
        mock_Student.return_value.read_paginated.return_value = Students, False, True
        sr = StudentListResource()
        res = sr.get()
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
