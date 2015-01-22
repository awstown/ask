# askutils.py

from askdb import ignores, warnings
from copy import deepcopy

class Friend(object):
    """A class to store friend information gathered from FB
       PARAMS: statuses is a list!
    """
    def __init__(self, name, statuses):
        self.name = name
        self.statuses = statuses

        # Clean Statuses
        words = []
        for status in statuses:
            word_list = status.lower().split()
            words.extend([i for i in word_list if i not in ignores])
        self.words = words

        # Determine if friend is depressed/suicidal
        warning_words = [w for w in words if w in warnings]
        self.warning_words = warning_words

        # add up the words weight
        rating = sum([warnings[k] for k in warning_words])
        self.rating = rating
