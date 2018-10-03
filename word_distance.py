#!/usr/bin/env python3

import itertools
import re


def find_shortest_distance(a, b, file_path):
    with open(file_path) as fp:
        text = fp.read()
    groups = re.findall(r'({})|({})|(\w+)'.format(a, b), text, flags=re.IGNORECASE)
    indexer = lambda x: [index for index, group in enumerate(groups) if group[x]]
    indices_a = indexer(0)
    indices_b = indexer(1)
    distances = (abs(index_a - index_b) for index_a, index_b in itertools.product(indices_a, indices_b))
    return min(distances)


if __name__ == '__main__':
    print(find_shortest_distance('motivation', 'development', 'sample.txt'))
