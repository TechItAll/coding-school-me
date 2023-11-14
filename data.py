import configparser,os
os.system("cls")

config = configparser.RawConfigParser()
config.read(r'FILE_PATH') # Filepath of the config file.

details_dict = dict(config.items('Hi'))
if details_dict.get('hw2') == '5':
    print('jgid')
print(details_dict)