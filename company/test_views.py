from django.test import TestCase
from django.urls import reverse

from company.models import Company


class TestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.company = Company(name='test', owner='test owner')
        cls.company.save()

    def test_delete_view_get(self):
        response = self.client.get(reverse('company:delete', kwargs={'pk': self.company.pk}))
        self.assertEquals(response.status_code, 200)

    def test_delete_view_post(self):
        response = self.client.post(reverse('company:delete', kwargs={'pk': self.company.pk}), follow=True)
        self.assertRedirects(response, reverse('company:list'), status_code=302)
