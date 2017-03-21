# unittesting the configParzolo.py

import unittest
from configParzolo import ConfigParsolo


class TestConfigParsolo(unittest.TestCase):
    def test_modify(self):
        config2 = ConfigParsolo('config.cfg')
        config2.config_modify('base', 'elso', 'unmodified')
        self.assertEqual('unmodified', config2.config_check('base', 'elso'))

        config2.config_modify('base', 'elso', 'modified')
        self.assertEqual('modified', config2.config_check('base', 'elso'))

    def test_check(self):
        config = ConfigParsolo('config2.cfg')
        self.assertIsNotNone(config)
        self.assertEqual(config.config_check('base', 'elso'), 'modified')

if __name__ == "__main__":
    unittest.main()
