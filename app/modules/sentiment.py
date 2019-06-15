# -*- coding: utf-8 -*-
"""
Created on Thus May 15 19:46:50 2019
Author: saurabh
"""

from textblob import TextBlob


class Sentiment:
    """ Sentiment Analysis

        the process of computationally identifying and categorizing opinions
        expressed in a piece of text, especially in order to determine whether
        the writer's attitude towards a particular topic, product, etc.
        is positive, negative, or neutral.

        Polarity is a float value within the range [-1.0 to 1.0]
        where 0 indicates neutral, +1 indicates a very positive sentiment
        and -1 represents a very negative sentiment.

        Subjectivity is a float value within the range [0.0 to 1.0]
        where 0.0 is very objective and 1.0 is very subjective.
        Subjective sentence expresses some personal feelings, views, beliefs,
        opinions, allegations, desires, beliefs, suspicions, and speculations
        where as Objective sentences are factual.
    """

    def __init__(self):
        pass

    def check_sentiment(self, text):

        analysis = TextBlob(text)

        if analysis.sentiment.polarity == 0:
            return 'Nuetral'
        elif analysis.sentiment.polarity < 0:
            return 'Negative'
        else:
            return 'Positive'
