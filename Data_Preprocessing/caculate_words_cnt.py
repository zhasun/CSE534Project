import os,sys
import math 
import string
import re
import os.path
import collections
from collections import defaultdict

reader = open(sys.argv[1])
data = reader.read().splitlines()

dic = collections.OrderedDict()
dic = defaultdict(lambda: 0, dic)


for i in range(len(data)):
	thread = data[i].split()
	for word in thread:
		dic[word] += 1

row_cnt = len(data)
coloum_cnt = len(dic)
#result = row_cnt*[coloum_cnt*[0]]
result = [[0 for i in xrange(coloum_cnt)] for i in xrange(row_cnt)]

for i in range(len(data)):
	thread = data[i].split()
	for word in thread:
		#print word+' :'+ str(dic.keys().index(word)) +' '+str(result[i][dic.keys().index(word)])+'\n'
		result[i][dic.keys().index(word)] += 1

writer = open('caculate_words_cnt.txt', 'w')

#for key,value in dic.items():
#	writer.write('\t'+key)

#writer.write('\n')

for i in range(row_cnt):
	#writer.write(str(i+1))
	for j in range(coloum_cnt):
		writer.write(str(result[i][j])+' ')
	writer.write('\n')
print "finish"
print result[0][4]

