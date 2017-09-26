from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertIn(b'Yummy Recipes', response.data)

    # Ensure that the signin page loads correctly
    def test_signin_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/signin', content_type='html/text')
        self.assertIn(b'Please sign in', response.data)

# Ensure that the signin page loads correctly
    def test_signup_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertIn(b'Sign Up Here', response.data)

if __name__ == '__main__':
    unittest.main()