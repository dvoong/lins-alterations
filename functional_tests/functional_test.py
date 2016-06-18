from selenium import webdriver
from django.test import 

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test(self):

        # load homepage
        self.browser.get(self.server)
        assert False, 'TODO'
