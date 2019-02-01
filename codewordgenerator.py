#!/usr/bin/env python3
# 
import random


def random_line(xfile):
	# Kudos to Alex Martelli and Martijn Pieters for the Waterman's Reservoir Algorithm code
	# https://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file-in-python
	line = next(xfile)
	for num, xline in enumerate(xfile, 2):
		if random.randrange(num): continue
		line = xline
	return line

def get_noun(nfile):
	# Noun list source
	# http://www.desiquintans.com/downloads/nounlist/nounlist.txt
	with open(nfile) as file:
		return random_line(file).strip()

def get_adj(afile):
	# Adjectives source list
	# https://www.talkenglish.com/vocabulary/top-500-adjectives.aspx
	with open(afile) as file:
		return random_line(file).strip()

def get_verb(vfile):
	# Verbs source list
	# https://www.linguasorb.com/english/verbs/most-common-verbs/1
	with open(vfile) as file:
		return random_line(file).strip()

def gen_code(nfile, afile,vfile):
	# kudos to Asim Ihsan (https://github.com/asimihsan) for the structure
	# of either two nouns or an adjective and a noun
	# https://gist.github.com/asimihsan/8239189
	# (n,n)
	# (a,n)
	num = random.randint(0,99)
	if num % 5 > 1:
		# (n,n)
		word1 = get_noun(nfile).upper()
		word2 = get_noun(nfile).upper()
		code = word1 + word2
		return code
	elif num % 5 == 1:
		# (a,n)
		word1 = get_adj(afile).upper()
		word2 = get_noun(nfile).upper()
		code = word1 + word2
		return code
	else:
		# (v,n)
		word1 = get_verb(vfile).upper()
		word2 = get_noun(nfile).upper()
		code = word1 + word2
		return code
		
def main():
	code = gen_code("nouns.txt","adjs.txt","verbs.txt")
	print(code)

if __name__ == "__main__":
	main()
