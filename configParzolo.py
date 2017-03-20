# Created by Daniel Nagy
#
# How to use example:
# you don't need a config.cfg file if you use a modify method!
#
# config = ConfigParsolo('config.cfg')
# print(config.config_lekeres('first', 'var1'))
# config2.config_modosito('base', 'elso', 'masodik')
# print(config2.config_lekeres('base', 'elso'))


import configparser


class ConfigParsolo:
    config = configparser.ConfigParser()
    config_file_name = ""

    def __init__(self, config_file_name):
        config = self.config
        self.config_file_name = config_file_name
        config.read(config_file_name)
        config.sections()

    def config_section_map(self, section):
        config = self.config
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except Exception as error_msg:
                print("exception on %s!" % option)
                print(error_msg)
                dict1[option] = None
        return dict1

    # Checking the config file's values

    def config_lekeres(self, szekcio2, mezo):
        szekcio = self.config_section_map(szekcio2)
        if szekcio[mezo] == 'True':
            return True
        elif szekcio[mezo] == 'False':
            return False
        elif szekcio[mezo] == 'None':
            return None
        else:
            return szekcio[mezo]

    # Modifying the config file

    def config_modosito(self, szekcio3, mezo1, uj_ertek):
        config = self.config
        config_file_name = self.config_file_name
        cfgfile = open(config_file_name, 'w')
        if uj_ertek is not None:
            config.set(szekcio3, mezo1, uj_ertek)
            config.write(cfgfile)
            cfgfile.close()
