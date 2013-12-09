from distutils.core import setup

setup(
    author='Jason Grosz',
    author_email='jgrosz@tinisi.com',
    name='confighelper',
    version='0.25dev',
    scripts = ['scripts/test_confighelper.py'],
    packages = ['confighelper','confighelper/tests'],
    package_data = {
        'confighelper': ['tests/test_file.txt','tests/test_json.json','tests/test_confighelper.json'],
    },
	license='BSD',
    long_description=open('README.md').read(),
    url='http://github.com/tinisi/confighelper'
)