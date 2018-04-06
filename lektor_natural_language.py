# -*- coding: utf-8 -*-
from nltk import tokenize
from rake_nltk import Rake

from lektor.pluginsystem import Plugin

class NaturalLanguagePlugin(Plugin):
    name = 'Natural Language'
    description = u'Template filters to do a little language processing with nltk.'

    def on_setup_env(self, **extra):
        def sentences_filter(txt):
            '''Accept a string of text and return a list of sentences in that text.
            '''
            return tokenize.punkt.PunktSentenceTokenizer().sentences_from_text(txt)
        self.env.jinja_env.filters['sentences'] = sentences_filter

        def firstsentence_filter(txt):
            '''Accept a string of text and return a list of sentences in that text.
            '''
            try:
                rv = sentences_filter(txt)[0]
            except IndexError:
                rv = None
            return rv
        self.env.jinja_env.filters['firstsentence'] = firstsentence_filter

        def keywords_filter(txt):
            '''Accept a string of txt and return a list of keywords used.
            '''
            r = Rake()
            try:
                r.extract_keywords_from_text(txt)
                rv = r.get_ranked_phrases()
            except TypeError:
                rv = None
            return rv
        self.env.jinja_env.filters['keywords'] = keywords_filter
