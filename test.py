from app import app
import unittest


class FlaskTest(unittest.TestCase):

    # Testing status code for API response
    def test_status_code(self):
        tester = app.test_client(self)
        response = tester.get('users/sonusood')
        status_code = response.status_code
        self.assertEqual(200, status_code)

    # Testing status code for 404 request
    def test_bad_request(self):
        tester = app.test_client(self)
        response = tester.get('users/sonusood/10')
        status_code = response.status_code
        self.assertEqual(404, status_code)

    # Testing content type of api response
    def test_content_type(self):
        tester = app.test_client(self)
        response = tester.get('users/sonusood')
        self.assertEqual('application/json', response.content_type)

    # Testing for data response type in response
    def test_response_data_type(self):
        tester = app.test_client(self)
        response = tester.get('users/sonusood')
        self.assertEqual(list, type(response.json))

    # Testing default number of tweets
    def test_default_tweets_number(self):
        tester = app.test_client(self)
        response = tester.get('users/sonusood')
        self.assertEqual(30, len(response.json))

    # Testing limit param
    def test_limit_param(self):
        tester = app.test_client(self)
        response = tester.get('users/sonusood?limit=10')
        self.assertEqual(10, len(response.json))

    # Testing href in response
    def test_user_href(self):
        tester = app.test_client(self)
        response = tester.get('users/sonusood?limit=10')
        self.assertEqual('/SonuSood', response.json[0]['account']['href'])


if __name__ == '__main__':
    unittest.main()
