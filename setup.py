import ast
import io
import re

from setuptools import setup

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r'description\s+=\s+(?P<description>.*)')

with open('lektor_natural_language.py', 'rb') as f:
    description = str(ast.literal_eval(_description_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    author='Terminal Labs',
    author_email='solutions@terminallabs.com',
    description='Adds NLTK based template filters.',
    keywords='Lektor plugin static-site nltk natrual-language jinja2 jinja filter',
    license='BSD-3-Clause',
    long_description=readme,
    long_description_content_type='text/markdown',
    name='lektor-natural-language',
    py_modules=['lektor_natural_language'],
    url='https://github.com/terminal-labs/lektor-natural-language',
    version='0.3.1',
    classifiers=[
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Lektor',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'lektor.plugins': [
            'natural-language = lektor_natural_language:NaturalLanguagePlugin',
        ]
    },
    install_requires=[
        'nltk',
        'rake-nltk'
    ]
)
