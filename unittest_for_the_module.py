# unittesting the configParzolo.py

import unittest

from configParzolo import configHandler


class TestConfigParsolo(unittest.TestCase):
    def test_modify(self):
        config2 = configHandler.ConfigHandler('config.cfg')
        config2.config_modify('base', 'first', 'unmodified')
        self.assertEqual('unmodified', config2.config_check('base', 'first'))

        config2.config_modify('base', 'first', 'modified')
        self.assertEqual('modified', config2.config_check('base', 'first'))

    def test_check(self):
        config = configHandler.ConfigHandler('config.cfg')
        self.assertIsNotNone(config)
        self.assertEqual(config.config_check('base', 'first'), 'modified')


if __name__ == "__main__":
    unittest.main()
