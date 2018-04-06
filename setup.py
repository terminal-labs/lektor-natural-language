from setuptools import setup

setup(
    name='lektor-natural-language',
    version='0.1',
    author='Terminal Labs',
    author_email='solutions@terminallabs.com',
    description='Adds NLTK based template filters.',
    license='BSD-3-Clause',
    py_modules=['lektor_natural_language'],
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
