## lektor-natural-language

This is a Lektor plugin that provides a few simple template filters with the Natural Language ToolKit (nltk).

This offers the following filters:

### `sentences_filter`

Accept a string of text and return a list of its sentences.

Usage: `{{ this.text|sentences }}`

### `firstsentences_filter`

Accept a string of text and return its the first sentence.

Usage: `{{ this.text|firstsentence }}`

### `sentences_filter`

Accept a string of text and return a list its keywords as determined by `nltk`'s `Rake`.

Usage: `{{ this.text|keywords }}`
