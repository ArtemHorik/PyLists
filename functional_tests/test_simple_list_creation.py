from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class NewVisitorTest(FunctionalTest):
    """NewVisitor Test"""

    def test_can_start_a_list_for_one_user(self):
        """Start a list and receive"""
        self.browser.get(self.live_server_url)
        # we see To Do title and header
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        print(header_text)
        self.assertEqual("Start a new To-Do list", header_text)
        # enter the list element
        input_box = self.get_item_input_box()
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            "Enter a to-do item"
        )
        # we enter the new item "apply to a job" in the input box
        self.create_list_item("Apply to a job")

        self.wait_for_row_in_list_table("1: Apply to a job")
        # we enter another item - "Go to lectures"
        self.create_list_item("Go to lectures")
        # now we see both elements in list
        self.wait_for_row_in_list_table("1: Apply to a job")
        self.wait_for_row_in_list_table("2: Go to lectures")

    def test_multiple_users_can_start_lists_at_different_urls(self):
        """test: Multiple users can start lists at different urls"""
        # first user
        self.browser.get(self.live_server_url)
        self.create_list_item("Go to lectures")
        self.wait_for_row_in_list_table("1: Go to lectures")
        # we see that our list has unique url
        first_user_url = self.browser.current_url
        self.assertRegex(first_user_url, '/lists/.+')

        # second user
        self.browser.quit()
        self.browser = webdriver.Edge()

        # we don't see previous list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Go to lectures', page_text)

        # we make a new list
        self.create_list_item("Buy milk")
        self.wait_for_row_in_list_table("1: Buy milk")

        # second user gets unique url
        second_user_url = self.browser.current_url
        self.assertRegex(second_user_url, '/lists/.+')
        self.assertNotEqual(first_user_url, second_user_url)

        # nothing from first user
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Go to lectures', page_text)
        self.assertIn("Buy milk", page_text)

