#!/usr/bin/env python3

import re


def find_shortest_distance(a, b, file_path):
    with open(file_path) as fp:
        text = fp.read()
    groups = re.findall(r'({})|({})|(\w+)'.format(a, b), text, flags=re.IGNORECASE)
    indexer = lambda x: [index for index, group in enumerate(groups) if group[x]]
    indices_a = indexer(0)
    indices_b = indexer(1)
    print(indices_a, indices_b)


if __name__ == '__main__':
    find_shortest_distance('motivation', 'development', 'sample.txt')
