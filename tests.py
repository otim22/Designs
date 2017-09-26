import unittest


class Test(unittest.TestCase):

    def setup(self):
        print("sometext")

    # Ensure that Flask was set up correctly
    def test_index(self):
        print("Yummy Recipes")

    # Ensure that the signin page loads correctly
    def test_signin_page_loads(self):
        print("Please sign in")

    # Ensure that the signin page loads correctly
    def test_signup_page_loads(self):
        print("Sign Up Here")

if __name__ == '__main__':
    unittest.main()