# -*- coding: utf-8 -*-
"""
Created on Thus May 30 15:46:56 2019
Author: saurabh
"""

import re
import string

from contractions import contractions_dict
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from pattern.en import suggest


class Sentiment:
    """ Sentiment Analysis

        the process of computationally identifying and categorizing opinions
        expressed in a piece of text, especially in order to determine whether
        the writer's attitude towards a particular topic, product, etc.
        is positive, negative, or neutral.
    """

    def __init__(self):
        pass

    def expand_contractions(self, text):
        pattern = re.compile(
            "({})".format( "|".join( contractions_dict.keys() ) ),
            flags=re.DOTALL | re.IGNORECASE )

        def replace_text(t):
            txt = t.group( 0 )
            if txt.lower() in contractions_dict.keys():
                return contractions_dict[txt.lower()]

        expand_text = pattern.sub( replace_text, text )
        return expand_text

    def remove_repeated_characters(self, word):
        pattern = re.compile( r"(\w*)(\w)\2(\w*)" )
        substitution_pattern = r"\1\2\3"
        while True:
            if wordnet.synsets( word ):
                return word
            new_word = pattern.sub( substitution_pattern, word )
            if new_word != word:
                word = new_word
                continue
            else:
                return new_word

    def spelling_checker(self, word):
        checker = suggest( word )
        return checker[0][0]

    def text_processing(self, input_data):
        # setting to lower
        input_data = input_data.lower()

        # removing urls from text
        # http matches literal characters
        # \S+ matches all non-whitespace characters (the end of the url)
        # we replace with the empty string
        input_data = re.sub( r"http\S+", "", input_data )

        # Fixes contractions such as `you're` to you `are`
        expanded_text = self.expand_contractions( input_data )

        # White spaces removal
        input_str = expanded_text.strip()

        # removing numbers
        number_free_text = re.sub( r'\d+', '', input_str )

        # Punctuation removal
        punctuation_free_text = number_free_text.translate(
            str.maketrans( '', '', string.punctuation ) )

        # converting sentence into tokens
        tokens = word_tokenize( punctuation_free_text )

        # removing stop words
        stop_words = set( stopwords.words( 'english' ) )

        nostopwods = [word for word in tokens if not word in stop_words]

        # morphological analysis of the words studies->study
        lemmatizer = WordNetLemmatizer()

        # Now just remove along with stemming words
        ps = PorterStemmer()
        nostemwords = [ps.stem( lemmatizer.lemmatize( word ) ) for word in
                       nostopwods]

        # keeping same order of text
        output = sorted( set( nostemwords ), key=nostemwords.index )

        # removing repeated words
        without_repeated_chars = [self.remove_repeated_characters( s ) for s in
                                  output]

        # correcting the spellings
        # output = [self.spelling_checker(s.lower()) for s in without_repeated_chars]

        clean_text = ' '.join( without_repeated_chars )
        return clean_text

    def prediction(self, text_data):

        clean_text = self.text_processing( text_data )
        return clean_text
