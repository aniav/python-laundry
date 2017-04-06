import os
import time

import numpy

from .comparators import (
    jaccard_similarity_ratio, levenshtein_similarity_ratio,
    sequence_matcher_similarity_ratio, sorensen_similarity_ratio)

LEVENSHTEIN = "Levenshtein"
SEQUENCE_MATCHER = "SequenceMatcher"
SORENSEN = "Sorensen"
JACCARD = "Jaccard"
COMPARATORS = [LEVENSHTEIN, SEQUENCE_MATCHER, SORENSEN, JACCARD]
NUM_DOCS = 1

resources_path = os.path.realpath(os.path.join(os.getcwd(), "resources"))

def get_cleaners():
    # TODO: make this generic loading all cleaners from the cleaners dir
    from .cleaners import boilerpipe, goose, justext, newspaper, tika
    return [boilerpipe, justext, newspaper, tika]

def get_contents(index):
    file_path = os.path.join(resources_path, "{}.html".format(index))
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def get_expected_content(index):
    file_path = os.path.join(resources_path, "{}.txt".format(index))
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def check_cleaners_quality():
    cleaners = get_cleaners()
    timings = {cleaner.__file__ : list() for cleaner in cleaners}

    results = {
        comparator: {cleaner.__file__: list() for cleaner in cleaners}
        for comparator in COMPARATORS}

    for cleaner in cleaners:
        cleaner_name = cleaner.__file__
        print(cleaner_name, end="")
        for i in [1]:
            print(".", end="")
            original_content = get_contents(i)
            expected_content = get_expected_content(i)

            start_time = time.time()
            actual_content = cleaner.clean(original_content)
            timings[cleaner_name].append(time.time() - start_time)
            if not actual_content:
                print("E", end="")
                continue

            results[LEVENSHTEIN][cleaner_name].append(
                levenshtein_similarity_ratio(
                    actual_content, expected_content))

            results[SEQUENCE_MATCHER][cleaner_name].append(
                sequence_matcher_similarity_ratio(
                    actual_content, expected_content))

            results[SORENSEN][cleaner_name].append(sorensen_similarity_ratio(
                actual_content, expected_content))

            results[JACCARD][cleaner_name].append(jaccard_similarity_ratio(
                actual_content, expected_content))
        print("")  # Newline

    row_format = "{:>15}" * (len(cleaners) + 1)
    print(row_format.format("", *map(lambda x: x.__file__, cleaners)))
    time_averages = [sum(timings[e.__file__])/NUM_DOCS for e in cleaners]
    print(row_format.format("AGV TIME", *time_averages))

    print(row_format.format("AGV QUALITY", *map(lambda x: "", cleaners)))
    for name, types in results.items():
        averages = [sum(types[e.__file__])/NUM_DOCS for e in cleaners]
        print(row_format.format(name, *averages))

    print(row_format.format("MEDIAN QUALITY", *map(lambda x: "", cleaners)))
    for name, types in results.items():
        averages = [numpy.median(types[e.__file__]) for e in cleaners]
        print(row_format.format(name, *averages))


if __name__ == "__main__":
    check_cleaners_quality()