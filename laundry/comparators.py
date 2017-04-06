""" Various tools to determine how much two strings are similar. """
from difflib import SequenceMatcher

import distance
import Levenshtein


def jaccard_similarity_ratio(actual_content, expected_content):
    return 1 - distance.jaccard(actual_content, expected_content)


def levenshtein_similarity_ratio(actual_content, expected_content):
    return Levenshtein.ratio(actual_content, expected_content)


def sequence_matcher_similarity_ratio(actual_content, expected_content):
    return SequenceMatcher(None, actual_content, expected_content).ratio()


def sorensen_similarity_ratio(actual_content, expected_content):
    return 1 - distance.sorensen(actual_content, expected_content)