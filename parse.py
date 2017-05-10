#!/usr/bin/python3

import os


def parse_file(path):
	data = []
	for line in open(path):
		spls = line.strip().replace(' ','').split('\t')
		year = int(spls[0].split('-')[0])
		for i in range((len(spls) - 1)//2):
			value = spls[2*i + 2]
			if len(value) > 0:
				date = spls[2*i + 1].split('/')
				data.append(((year, int(date[0]), int(date[1])), float(value)))
	name = path.split('/')[-1].split('.')[0]
	return (name, data)

def parse_dir(path):
	fns = os.listdir(path)
	return [parse_file(path + '/' + fn) for fn in fns]
