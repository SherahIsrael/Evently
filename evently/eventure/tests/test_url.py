from django.test import SimpleTestCase
from django.urls import reverse, resolve
from eventure.views import home, events, users, usersDetails


class testUrls(SimpleTestCase):
    # test if the named url calls to the correct view
    def testEventUrlIsResolved(self):
        url = reverse("events")
        print(resolve(url))
        self.assertEqual(resolve(url).func, events)

    def testHomeUrlIsResolved(self):
        url = reverse("home")
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)

    def testUsersUrlIsResolved(self):
        url = reverse("users")
        print(resolve(url))
        self.assertEqual(resolve(url).func, users)

    def testDetailsUrlIsResolved(self):
        url = reverse('eventDetails', args=['user-slug'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, usersDetails)
