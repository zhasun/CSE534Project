import os, sys
path = "."
dirs = os.listdir( path )
Nline=""
NNline=""
count = 0
pre_line =""
next_line=""
total_thread = 0
for filename in dirs:
	count = 0
	if filename == "Readme" or filename == "count_thread.py":
		continue
	with open(filename, "r") as f:
		lines = f.readlines()
		for line in lines:
			word = line.split()
			if word and word[0]=="END":
				count+=1
				total_thread+=1
	print filename +" has "+ str(count) + " threads."
print "Total_thread = "+str(total_thread)


