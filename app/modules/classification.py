# -*- coding: utf-8 -*-
"""
Created on Thus May 30 15:46:56 2019
@author: saurabh
"""

import re
import string

from contractions import contractions_dict
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize


# https://www.linkedin.com/pulse/processing-normalizing-text-data-saurav-ghosh/


class Sentiment:

    def __init__(self):
        pass

    def expand_contractions(self, text):
        pattern = re.compile("({})".format("|".join(contractions_dict.keys())),
                             flags=re.DOTALL | re.IGNORECASE)

        def replace_text(t):
            txt = t.group(0)
            if txt.lower() in contractions_dict.keys():
                return contractions_dict[txt.lower()]

        expand_text = pattern.sub(replace_text, text)
        return expand_text

    def text_processing(self, input_data):
        # setting to lower
        input_data = input_data.lower()

        # Fixes contractions such as `you're` to you `are`
        expanded_text = self.expand_contractions(input_data)

        # White spaces removal
        input_str = expanded_text.strip()

        # removing numbers
        number_free_text = re.sub(r'\d+', '', input_str)

        # Punctuation removal
        punctuation_free_text = number_free_text.translate(
            str.maketrans('', '', string.punctuation))

        # converting sentence into tokens
        tokens = word_tokenize(punctuation_free_text)

        # removing stop words
        stop_words = set(stopwords.words('english'))

        nostopwods = [word for word in tokens if not word in stop_words]

        # morphological analysis of the words studies->study
        lemmatizer = WordNetLemmatizer()

        # Now just remove along with stemming words
        ps = PorterStemmer()
        nostemwords = [ps.stem(lemmatizer.lemmatize(word)) for word in
                       nostopwods]

        # keeping same order of text
        clean_text = sorted(set(nostemwords), key=nostemwords.index)

        clean_text = ' '.join(clean_text)

        return clean_text

    def prediction(self, text_data):
        clean_text = self.text_processing(text_data)

        return clean_text
