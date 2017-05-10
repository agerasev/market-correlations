#!/usr/bin/python3

from parse import *
from algo import *
from tree import *

charts = parse_dir('prices')
distances = distance(correlations([nc[1] for nc in charts]))
tree = min_spanning_tree(distances)
print_tree(["{%s}" % nc[0].split(',')[0] for nc in charts], tree, len(charts) - 1)
