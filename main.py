import unittest
from configParzolo import ConfigParsolo


class TestConfigParsolo(unittest.TestCase):
    def test_modify(self):
        config2 = ConfigParsolo('config.cfg')
        config2.config_modosito('base', 'elso', 'unmodified')
        print('before modify: '+config2.config_lekeres('base', 'elso'))
        config2.config_modosito('base', 'elso', 'modified')
        print('after modify: '+config2.config_lekeres('base', 'elso'))

    def test_check(self):
        config = ConfigParsolo('config2.cfg')
        print('Check config file: '+config.config_lekeres('base', 'elso'))

if __name__ == "__main__":
    unittest.main(verbosity=2)
