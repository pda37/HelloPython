import unittest
import requests


class TestGlh(unittest.TestCase):
    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('teardown')

    def test_StatusCodeIs200(self):
        payload = {'page': 1, 'size': 20}
        url = 'https://test.gelonghui.com/api/topContent/list'
        r = requests.get(url, params=payload)
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
