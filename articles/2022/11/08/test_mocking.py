import unittest
from unittest import mock

import check_some_mock


class TestStudents(unittest.TestCase):

    def test_if_student_is_learning(self):
        self.assertTrue(check_some_mock.GetStudent('Bob').lern())

    def test_if_students_name(self):
        self.assertListEqual(['Bob', 'John', 'Tom'],
                             check_some_mock.GetMultipleStudents())

    # def test_some_mock_fun(self):
    #     with mock.patch.object(check_some_mock.GetStudent('Bob'),
    #                            'get_my_name',
    #                            return_value='Hmmmmm'):
    #         self.assertListEqual(['Bob', 'John', 'Tom'],
    #                     check_some_mock.GetMultipleStudents())

    # def test_some_mock_fun_but_with_side_effects(self):
    #     with mock.patch.object(check_some_mock.GetStudent('Bob'),
    #                            'get_my_name',
    #                            side_effect=['Hmmmmm', ':)', ':P']):
    #         self.assertListEqual(['Bob', 'John', 'Tom'],
    #                     check_some_mock.GetMultipleStudents())

    def test_check_some_student(self):

        with mock.patch.object(check_some_mock.GetStudent('Tom'),
                        'get_my_name',
                        return_value='Bob'):
            self.assertEqual(check_some_mock.GetStudent('Tom').get_my_name(), 'Bob')


if __name__ == '__main__':
    unittest.main()
