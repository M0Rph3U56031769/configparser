import configParsolo

from configParzolo import ConfigParsolo

print('var1 értéke: '+configParsolo.configLekeres('first', 'var1'))

#config = ConfigParsolo('config.cfg')
#print(config.config_lekeres('first', 'var1'))

config2 = ConfigParsolo('config2.cfg')
print(config2.config_lekeres('base', 'elso'))
config2.config_modosito('base', 'elso', 'masodik')
print(config2.config_lekeres('base', 'elso'))
