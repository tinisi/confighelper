
import json

# magic stringses...
SHARED_CONF_KEY = 'shared_conf'
HOST_CONF_KEY = 'host_conf'

class ConfigHelper:
    """
    This helper class will return shared config or config for the current host.

    Initialize with the full path to a config file and the
    name of the current host.

    The config file should be a json document with this shape:
    {
        "shared_conf": {
            "key": "value"
        },
        "host_conf": {
            "env.host": {
                "key": "value"
            }
        }
    }

    If you are using this with Fabric, init it with env.host.
    """

    def __init__(self, config_file, host):
        # set the host attribute
        self.host=host
        # import the config file
        # TODO: make this easier to test
        with open(config_file) as config_file:
            self.config_data = json.load(config_file)

    def get_conf(self, key):
        return self.config_data[SHARED_CONF_KEY][key]

    def get_host_conf(self, key):
        return self.config_data[HOST_CONF_KEY][self.host][key]

__all__ = ['ConfigHelper']
