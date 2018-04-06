from setuptools import setup

setup(
    name='lektor-natural-language',
    version='0.1',
    author='Terminal Labs',
    author_email='solutions@terminallabs.com',
    license='MIT',
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
