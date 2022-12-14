from django.core.exceptions import ValidationError
from django.test import TestCase
from app.models import Item, List


class ListAndItemModelTest(TestCase):
    """List item model test"""

    def test_default_text(self):
        """test: default text"""
        item = Item()
        self.assertEqual(item.text, "")

    def test_item_is_related_to_list(self):
        """test: item is related to list"""
        list_ = List.objects.create()
        item = Item()
        item.list = list_
        item.save()
        self.assertIn(item, list_.item_set.all())

    def test_cannot_save_empty_list_items(self):
        """test: can't save an empty list item"""
        list_ = List.objects.create()
        item = Item(list=list_, text="")
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_duplicate_items_are_invalid(self):
        """test: duplicate items are invalid"""
        list_ = List.objects.create()
        Item.objects.create(list=list_, text="dude")
        with self.assertRaises(ValidationError):
            item = Item(list=list_, text="dude")
            item.full_clean()

    def test_CAN_save_item_to_different_lists(self):
        """test: CAN save same item to different lists"""
        list_1 = List.objects.create()
        list_2 = List.objects.create()
        Item.objects.create(list=list_1, text="dude")
        item = Item(list=list_2, text="dude")
        item.full_clean()  # should not raise exception

    def test_list_ordering(self):
        """test: list ordering"""
        list_1 = List.objects.create()
        item1 = Item.objects.create(list=list_1, text="i1")
        item2 = Item.objects.create(list=list_1, text="it 2")
        item3 = Item.objects.create(list=list_1, text="3")
        self.assertEqual(
            list(Item.objects.all()),
            [item1, item2, item3]
        )

    def test_string_representation(self):
        """test: string representation"""
        item = Item(text='some text')
        self.assertEqual(str(item), 'some text')


class ListModelTest(TestCase):
    """List model test"""

    def test_get_absolute_url(self):
        """test: get absolute url"""
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')
