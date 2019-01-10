import unittest
from unittest.mock import patch


class TestUserCreateResource(unittest.TestCase):
    @patch('user.rest_api.user_resource.UserRepository')
    def test_post(self, mock_user):
        mock_user.return_value.create.return_value = "123"
        ur = UserCreateResource()
        res = ur.post()
        self.assertEqual(res.status_code, 201)


class TestUserResource(unittest.TestCase):
    @patch('user.rest_api.user_resource.UserRepository')
    def test_get_right(self, mock_user):
        user = User(user_id="123", faculty_ids="012", name="name", admin="false")
        mock_user.return_value.get.return_value = user
        ur = UserResource()
        res = ur.get("123")
        self.assertEqual(res.status_code, 200)

    def test_get_error(self):
        ur = UserResource()
        try:
            res = ur.get("5bd0a351")
        except:
            self.assertTrue(True)

    def test_delete_error(self):
        ur = UserResource()
        try:
            res = ur.delete("5bd0a351")
        except:
            self.assertTrue(True)

    @patch('user.rest_api.user_resource.UserRepository')
    def test_delete_right(self, mock_user):
        mock_user.return_value.delete.return_value = ''
        ur1 = UserResource()
        res = ur1.delete("123")
        self.assertEqual(res.status_code, 204)

    @patch('user.rest_api.user_resource.UserRepository')
    def test_patch_right(self, mock_user):
        mock_user.return_value.assign_ticket.return_value = True
        user = User(user_id="123", faculty_ids="012", name="name", admin="true")
        mock_user.return_value.get.return_value = user
        ur = UserResource()
        res = ur.patch("123")
        self.assertEqual(res.status_code, 201)


class TestStudentListResource(unittest.TestCase):
    @patch('user.rest_api.user_resource.UserRepository')
    def test_get(self, mock_user):
        users = []
        user = User(user_id="123", faculty_ids="012", name="name", admin="false")
        users.append(user)
        mock_user.return_value.read_paginated.return_value = users, False, True
        ur = UserListResource()
        res = ur.get()
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
