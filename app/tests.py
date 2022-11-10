from django.test import TestCase

from .models import Item


class HomePageTest(TestCase):
    """Home page test"""

    def test_uses_home_page(self):
        "test: home page returns correct html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        """test: can save a POST request"""
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        """test: redirects after a POST request"""
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/lists/unique-list/')

    def test_only_saves_items_when_necessary(self):
        """test: only saves items when necessary"""
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class ListViewTest(TestCase):
    """ListView test"""

    def test_uses_list_template(self):
        """test: uses list template"""
        response = self.client.get('/lists/unique-list/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        """test: displays all items"""
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        response = self.client.get('/lists/unique-list/')

        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')



class ItemModelTest(TestCase):
    """List item model test"""

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(len(saved_items), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(second_saved_item.text, "Item the second")
