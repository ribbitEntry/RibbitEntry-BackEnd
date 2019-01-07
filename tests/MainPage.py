import unittest
from server.view.mainPage.MainPage import MainPage


class MainPageTest(unittest.TestCase):

    def test_get(self):
        c = MainPage.get
        self.assertEqual(c, '')

    pass        