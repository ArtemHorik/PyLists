from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """NewVisitor Test"""

    def setUp(self):
        """Set up"""
        self.browser = webdriver.Edge()
        self.base_url = "http://localhost:8000"

    def tearDown(self):
        """Tear down"""
        self.browser.quit()

    def test_start_a_list_and_receive_it_later(self):
        """Start a list and receive"""
        self.browser.get(self.base_url)
        # we see To Do title and header
        self.assertIn("To-Do", self.browser.title)
        self.fail("Stop test!")


if __name__ == "__main__":
    unittest.main(warnings='ignore')
