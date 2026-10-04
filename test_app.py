import unittest

from app import app


class AppTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Sample Counters", res.data)

    def test_metrics(self):
        res = self.client.get("/metrics")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"http_requests_total", res.data)
        self.assertIn(b"db_connections", res.data)


if __name__ == "__main__":
    unittest.main()
