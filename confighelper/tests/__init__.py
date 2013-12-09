
import unittest
import json
import os
from confighelper import ConfigHelper

current_path = os.path.dirname(__file__)

TEST_HOST_NAME = 'test.tinisi.local'

class TestConfigHelper(unittest.TestCase):

    def test_file_read(self):

        test_file = '%(cp)s/test_file.txt' % { 'cp': current_path }
        
        file_contents = open(test_file).read()
        
        self.assertEqual(file_contents, 'test')

    def test_json_load(self):

        config_file = '%(cp)s/test_json.json' % { 'cp': current_path }
        
        with open(config_file) as config_file:
            test_config_data = json.load(config_file)
        self.assertEqual(test_config_data['test_value'], 'BOB')

    def test_shared(self):

        config_file = '%(cp)s/test_confighelper.json' % { 'cp': current_path }
        
        ch = ConfigHelper(config_file, TEST_HOST_NAME)

        shared_value = ch.get_conf('test');
        self.assertEqual(shared_value, True)

    def test_host_number(self):

        config_file = '%(cp)s/test_confighelper.json' % { 'cp': current_path }
        
        ch = ConfigHelper(config_file, TEST_HOST_NAME)

        host_num = ch.get_host_conf('number');
        self.assertEqual(host_num, 3)

    def test_host_string(self):

        config_file = '%(cp)s/test_confighelper.json' % { 'cp': current_path }
        
        ch = ConfigHelper(config_file, TEST_HOST_NAME)

        host_str = ch.get_host_conf('string');
        self.assertEqual(host_str, 'test')

    def test_host_list(self):

        config_file = '%(cp)s/test_confighelper.json' % { 'cp': current_path }
        
        ch = ConfigHelper(config_file, TEST_HOST_NAME)

        host_list = ch.get_host_conf('list');
        self.assertEqual(host_list, [ 1, 2, 3 ] )

    def test_host_dict(self):

        config_file = '%(cp)s/test_confighelper.json' % { 'cp': current_path }
        
        ch = ConfigHelper(config_file, TEST_HOST_NAME)

        host_dict = ch.get_host_conf('dict');
        self.assertTrue(host_dict == { 'name_one': 'value_one' })

__all__ = ['TestConfigHelper']
