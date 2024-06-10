from django.test import SimpleTestCase
from django.urls import reverse, resolve
from eventure.views import home, events, users, details


class testUrls(SimpleTestCase):
    # test if the named url calls to the correct view
    def testHomeUrlIsResolved(self):
        url = reverse('events')
        print(resolve(url))
        self.assertEqual(resolve(url).func, events)
