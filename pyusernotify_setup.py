import configparser

def pyusernotify_setup(setupfile="setup.ini"):
    config = configparser.ConfigParser()
    config['Default'] = {
        'SmtpServer': 'lsmtp.oakland.edu',
        'DefaultFromAddress': 'uts@oakland.edu',
        'webServicePort': '2400'}

    with open(setupfile, 'w') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    pyusernotify_setup()
