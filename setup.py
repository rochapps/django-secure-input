import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


setup(
    name='django-secure-input',
    version=__import__('secure_input').__version__,
    author='RochApps, LLC',
    author_email='info@rochapps.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/rochapps/django-secure-input/',
    license='BSD',
    description=u' '.join(__import__('secure_input').__doc__.splitlines()).strip(),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'Programming Language :: Python',      
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=read_file('README.rst'),
    install_requires=['bleach>=1.2.2', 'Markdown==2.3.1'],
    test_suite="runtests.runtests",
    tests_require=(
        'bleach>=1.2.2',
    ),
    zip_safe=False,
)
