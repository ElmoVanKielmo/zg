#!/usr/bin/env python3

import argparse
import itertools
import re


def find_shortest_distance(a, b, file_path):
    with open(file_path) as fp:
        text = fp.read()
    groups = re.findall(r'({})|({})|(\w+)'.format(a, b), text, flags=re.IGNORECASE)
    indexer = lambda x: [index for index, group in enumerate(groups) if group[x]]
    indices_a = indexer(0)
    indices_b = indexer(1)
    distances = (
        abs(index_a - index_b) - 1
        for index_a, index_b
        in itertools.product(indices_a, indices_b)
    )
    return min(distances)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', dest='file_path', default='sample.txt',
        help='Path to text file to be analyzed'
    )
    parser.add_argument(
        dest='words', metavar='word', type=str, nargs=2,
        help='Words to find distance between'
    )
    options = parser.parse_args()
    print(find_shortest_distance(*options.words, options.file_path))
