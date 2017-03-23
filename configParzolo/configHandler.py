# Created by Daniel Nagy
#
# How to use example:
# you don't need a config.cfg file if you use a modify method!
#
# config = ConfigParsolo('config.cfg')
# print(config.config_lekeres('first', 'var1'))
# config2.config_modosito('base', 'elso', 'masodik')
# print(config2.config_lekeres('base', 'elso'))

try:
    import configparser
except ImportWarning and ImportError as error_msg:
    print('Import at error: '+error_msg)
    print('You can solve it by downloading configparser: pip install configparser')


class ConfigHandler:
    config = configparser.ConfigParser()
    config_file_name = ""

    def __init__(self, config_file_name):
        config = self.config
        self.config_file_name = config_file_name
        config.read(config_file_name)
        config.sections()

    def config_section_map(self, section):
        config = self.config
        section_map = {}
        options = config.options(section)
        for option in options:
            try:
                section_map[option] = config.get(section, option)
                if section_map[option] == -1:
                    print("skip: %s" % option)
            except Exception as ERROR_MSG:
                print("exception on %s!" % option)
                print(ERROR_MSG)
                section_map[option] = None
        return section_map

    # Checking the config file's values

    def config_check(self, section, field):
        section_local = self.config_section_map(section)
        if section_local[field] == 'True':
            return True
        elif section_local[field] == 'False':
            return False
        elif section_local[field] == 'None':
            return None
        else:
            return section_local[field]

    # Modifying the config file

    def config_modify(self, section, field, new_value):
        config = self.config
        config_file_name = self.config_file_name
        cfgfile = open(config_file_name, 'w')
        if new_value is not None:
            config.set(section, field, new_value)
            config.write(cfgfile)
            cfgfile.close()
