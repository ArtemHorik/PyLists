from django.test import TestCase

from app.forms import ItemForm, EMPTY_ITEM_ERROR


class ItemFormTest(TestCase):
    """Tests form for list item"""

    def test_form_item_input_has_placeholder_and_css_classes(self):
        """test: form item input has placeholder and css classes"""
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control-lg w-50 border-info', form.as_p())

    def test_form_validation_for_blank_items(self):
        """test: form validation for blank items"""
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])

