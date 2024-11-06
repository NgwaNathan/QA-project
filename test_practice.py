import unittest
from practice import app



class FlaskAppTests(unittest.TestCase):
  

 def setUp(self):
        self.practice = app.test_client()
        self.practice = app.test_client()


def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Hello, World!'})

if __name__ == "__main__":
    unittest.main()