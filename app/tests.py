from django.test import TestCase


class SmokeTest(TestCase):
    """Tests for toxicity"""

    def test_bad_maths(self):
        """Test wrong math answers"""
        self.assertEqual(1 + 1, 3)

