from django.test import TestCase

from app.forms import ItemForm, EMPTY_ITEM_ERROR
from app.models import List, Item

class ItemFormTest(TestCase):
    """Tests form for list item"""

    def test_form_item_input_has_placeholder_and_css_classes(self):
        """test: form item input has placeholder and css classes"""
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control-lg w-75 border-info placeholder-wave"', form.as_p())

    def test_form_validation_for_blank_items(self):
        """test: form validation for blank items"""
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])

    def test_form_save_handles_saving_to_a_list(self):
        """test: form save handles saving to a list"""
        list_ = List.objects.create()
        form = ItemForm(data={'text': 'do me'})
        new_item = form.save(for_list=list_)
        self.assertEqual(new_item, Item.objects.first())
        self.assertEqual(new_item.text, 'do me')
        self.assertEqual(new_item.list, list_)
