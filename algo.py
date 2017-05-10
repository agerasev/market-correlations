#!/usr/bin/python3

import math


def one_correlation(rets, avgs, sqrs):
	n = len(rets[0])
	c = sum((rets[0][i] - avgs[0])*(rets[1][i] - avgs[1]) for i in range(n))/(sqrs[0]*sqrs[1])
	return max(min(c, 1.0), 0.0)

def correlations(charts):
	dates = []
	cookies = [[ch, 0, []] for ch in charts]
	done = False
	while not done:
		date = None
		for c in cookies:
			if len(c[0]) <= c[1]:
				done = True
				break
			cd = c[0][c[1]][0]
			if date is None or date < cd:
				date = cd
		if done:
			break

		eq = True
		for c in cookies:
			cd = c[0][c[1]][0]
			if cd < date:
				c[1] += 1
				eq = False
		if eq:
			dates.append(date)
			for c in cookies:
				c[2].append(c[0][c[1]][1])
				c[1] += 1
	prices = [c[2] for c in cookies]
	rets = [[math.log(p[i]) - math.log(p[i-1]) for i in range(1,len(p))] for p in prices]
	avgs = [sum(r)/(len(dates)-1) for r in rets]
	sqrs = [math.sqrt(sum((v - a)**2 for v in vs)) for vs, a in zip(rets, avgs)]
	return [[one_correlation(*zip(t0, t1)) for t0 in zip(rets, avgs, sqrs)] for t1 in zip(rets, avgs, sqrs)]

def distance(correlations):
	return [[math.sqrt(2*(1.0 - c)) for c in cs] for cs in correlations]