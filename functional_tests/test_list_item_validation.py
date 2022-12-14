from .base import FunctionalTest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from unittest import skip


class ItemValidationTest(FunctionalTest):
    """Test list item validation"""

    def get_error_element(self):
        """Returns error element"""
        return self.browser.find_element(By.CSS_SELECTOR, ".has-error")

    def test_cannot_add_empty_list_items(self):
        """test cannot add empty list items"""
        # we open home page and try to press Enter
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Browser don't let us add empty list items
        # page does not refresh
        self.wait_for(lambda: self.browser.find_element(
            By.CSS_SELECTOR, "#id_text:invalid"
        ))

        # now we start entering text and error message disappears
        self.get_item_input_box().send_keys("Buy milk")
        self.wait_for(lambda: self.browser.find_element(
            By.CSS_SELECTOR, "#id_text:valid"
        ))

        # and we can send it
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")

        # now we try to create empty list item again
        self.get_item_input_box().send_keys(Keys.ENTER)

        # and browser still doesn't let us do that
        self.wait_for_row_in_list_table("1: Buy milk")
        self.wait_for(lambda: self.browser.find_element(
            By.CSS_SELECTOR, "#id_text:invalid"
        ))

        # but we can fix it by adding some text
        self.get_item_input_box().send_keys("Make tea")
        self.wait_for(lambda: self.browser.find_element(
            By.CSS_SELECTOR, "#id_text:valid"
        ))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")
        self.wait_for_row_in_list_table("2: Make tea")

    def test_cannot_add_duplicate_items(self):
        """test: cannot add duplicate items"""
        # we open home page and start a new list
        self.browser.get(self.live_server_url)
        self.create_list_item("Buy carrot")
        self.wait_for_row_in_list_table("1: Buy carrot")

        # accidentally we add the same item
        self.create_list_item("Buy carrot")

        # then we see useful error message
        self.wait_for(lambda: self.assertEqual(
            self.get_error_element().text,
            "You've already got this in your list"
        ))

    def test_error_messages_are_cleared_on_input(self):
        """test: error messages are cleared on input"""
        # we open home page and trigger validation error
        self.browser.get(self.live_server_url)
        self.create_list_item("Learn JS")
        self.wait_for_row_in_list_table("1: Learn JS")
        self.create_list_item("Learn JS")

        self.wait_for(lambda: self.assertTrue(
            self.get_error_element().is_displayed()
        ))
        # we start typing to get rid of error
        self.get_item_input_box().send_keys("c")

        # we see that error disappears
        self.wait_for(lambda: self.assertFalse(
            self.get_error_element().is_displayed()
        ))
