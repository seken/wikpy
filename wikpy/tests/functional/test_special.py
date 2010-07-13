from wikpy.tests import *

class TestSpecialController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='special', action='index'))
        # Test response...
