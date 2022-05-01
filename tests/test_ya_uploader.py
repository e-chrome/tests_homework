import unittest
from ya_uploader import get_link

true_token = 'C:/codding/test_projects/tests_hw/tokens/ya_disk_token.txt'
false_token = 'C:/codding/test_projects/tests_hw/tokens/false_token.txt'


class TestFunctions(unittest.TestCase):
    def setUp(self):
        print('method setUp')

    def tearDown(self):
        print('method tearDown')

    def test_get_link_true_token(self):
        self.assertEqual(get_link(disk_file_path='/test_hw/', token_path=true_token), 200)

    def test_get_link_failure_token(self):
        self.assertEqual(get_link(disk_file_path='/test_hw/', token_path='text.txt'), 'token failure')

    def test_get_link_false_token(self):
        self.assertEqual(get_link(disk_file_path='/test_hw/', token_path=false_token), 401)


if __name__ == '__main__':
    unittest.main()