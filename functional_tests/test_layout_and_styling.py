from .base import FunctionalTest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class LayoutAndStylingTest(FunctionalTest):
    """Test layout and styling"""

    def test_layout_and_styling(self):
        """test layout and styling"""
        # we open home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # input box is perfectly centered
        input_box = self.get_item_input_box()
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            512,
            delta=40
        )
