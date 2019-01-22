import unittest
from server.view.page.mainPage import MainPage


class MainPageTest(unittest.TestCase):

    def test_get(self):
        c = MainPage.get
        self.assertEqual(c, '')

    pass        