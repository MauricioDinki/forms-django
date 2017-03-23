from django.test import TestCase

class CoolTest(TestCase):
    def setUp(self):
        print("\n setUp Function")

    def test_function(self):
        """Test passing."""
        print("\n Test function")
        self.assertEqual(True, True)
