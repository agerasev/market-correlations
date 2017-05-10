#!/usr/bin/python3

def min_spanning_tree(distances):
	n = len(distances)
	added = [False]*n
	tree = [[False]*n for _ in range(n)]

	added[0] = True
	for k in range(n - 1):
		ms, md, mv = None, None, None
		for s in range(n):
			if not added[s]:
				continue
			for d in range(n):
				if added[d]:
					continue
				v = distances[s][d]
				if mv is None or v < mv:
					mv = v
					ms = s
					md = d
		tree[ms][md] = True
		tree[md][ms] = True
		added[md] = True

	return tree

def print_tree(names, tree, trunk=0, parent=None, pattern='', prefix=('','')):
	n = len(names)
	s = prefix[0] + names[trunk]
	chs = [i for i in range(n) if i != parent and tree[trunk][i]]
	if len(chs) == 0:
		s += '\n'
	print(s, end='')
	pt = "%s%s%s" % (pattern, prefix[1], ' '*len(names[trunk]))
	for ch in chs:
		pr = ('','')
		if ch == chs[0]:
			if len(chs) > 1:
				pr = ('┬','│')
			else:
				pr = ('─',' ')
		elif ch == chs[-1]:
			pr = ('└',' ')
		else:
			pr = ('├','│')
		print_tree(names, tree, ch, trunk, pt, pr)
		if ch != chs[-1]:
			print(pt, end='')
