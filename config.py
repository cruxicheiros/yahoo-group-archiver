import configparser

class ConfigError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Config:
    def importIni(filename='config.ini'):
        # Uses type of initial value in config_structure to determine type to convert to.
        config_structure = {
                    'credentials': {
                            'y_cookie': str,
                            'p_cookie': str
                        },
                    'failure': {
                            'failure_timeout': int
                            'failure_tries': int
                        }
                }

        config = configparser.ConfigParser()
        config.read(filename)
        
        formatted_config = {}

        # Iterate over first keys and values
        for section, contents in config_structure:
            if section in config:
                formatted_config[section] = {}
                
                # Iterate over second set of keys and values
                for label, value_type in section:
                    if label in config[section]:
                        # Convert input to required type if it isn't already string
                        if (value_type != str):
                            formatted_config[section][label] = value_type(config[section][label])
                        else:
                            formatted_config[section][label] = config[section][label]

                    else:
                        raise ConfigError(filename + ' is missing "' + label + '" under the section [' + section + '].')
            else:
                raise ConfigError(filename + ' is missing the section [' + section + '].')


        return formatted_config




