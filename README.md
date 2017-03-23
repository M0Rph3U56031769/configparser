# configparser-light - configParsolo

This is an easy-to-use user-friendly version of the original configparser. It has two methods for use(config_check and config_modify).

Usage:
- copy the configParzolo.py file to the libs folder or where you want to use it.
- import the modul: from configParzolo import ConfigParsolo
- create an object and give a config file name: config = ConfigParsolo('config.cfg')
- check somthing from the config file: config.config_check('section', 'variable')
- modify something in the config file: config.config_modify('section', 'variable', 'new value')



Author: Daniel Nagy

https://github.com/M0Rph3U56031769/configparser
