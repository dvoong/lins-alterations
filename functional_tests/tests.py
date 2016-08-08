from .functional_test import FunctionalTest

class FunctionalTest(FunctionalTest):

    def test(self):
        url = self.live_server_url
        self.browser.get(url)
        title = self.browser.title
        self.assertEqual(title, '''Lin's Alterations''')

        # Prices
        # Location
        # Contact
