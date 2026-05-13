from django.test import TestCase
from form_example.models import Publisher

class PublisherModelTest(TestCase):
    def setUp(self):
        Publisher.objects.create(
            name="Publisher Name1",
            website="http://www.publisher.example.com",
            email="pub@example.com"
        )
        Publisher.objects.create(
            name="Publisher Name2",
            website="hhh://example.com",
            email="public@example.com"
        )

    def test_create_publisher_in_db(self):
        publisher1 = Publisher.objects.get(name="Publisher Name1")
        publisher2 = Publisher.objects.get(name="Publisher Name2")
        self.assertEqual(publisher1.name, "Publisher Name1")
        self.assertNotEqual(publisher2, "Publisher Name2")
