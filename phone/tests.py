from django.test import TestCase
from django.urls import reverse
from .forms import *


class NumberFormTest(TestCase):

    def test_PhoneForm_valid(self):
        form = PhoneForm(data={'text': """(850) 555 - 1212
                                       8505551213
                                       850.572.1214
                                       +1 850.572.1234
                                       6124686
                                       (702)1112323 and some of the phone numbers have text on the same line
                                       and the text keeps going
                                       702 612 4686
                                       and there are some dates like 12.01.2016 and 20160105
                                       adfasdfasdfasdf"""})
        self.assertTrue(form.is_valid())

    def test_add_phone_form_view(self):
        url = reverse('phone')
        response = self.client.post(url, {'text': "(850) 555 - 1212 8505551213 850.572.1214 +1 850.572.1234 6124686 (702)1112323 and some of the phone numbers have text on the same line and the text keeps going 702 612 4686 and there are some dates like 12.01.2016 and 20160105 adfasdfasdfasdf"}, format='json')
        self.assertEqual(response.status_code, 200)
