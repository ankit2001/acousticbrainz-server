from webserver.testing import AcousticbrainzTestCase
from webserver import utils


class UtilsTestCase(AcousticbrainzTestCase):

    def test_generate_string(self):
        length = 42
        str_1 = utils.generate_string(length)
        str_2 = utils.generate_string(length)

        self.assertEqual(len(str_1), length)
        self.assertEqual(len(str_2), length)
        self.assertNotEqual(str_1, str_2)  # Generated strings shouldn't be the same
