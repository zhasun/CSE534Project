import os, sys
path = "."
dirs = os.listdir( path )
Nline=""
NNline=""
count = 0
pre_line =""
next_line=""
for filename in dirs:
	with open(filename, "r") as f:
		lines = f.readlines()
		for index in range(len(lines)):
			if index > 0:
				pre_line = lines[index-1]
			if index < len(lines)-1:
				next_line = lines[index+1]
			if pre_line and next_line:
				if pre_line =="###############################################################\n"\
					and next_line=="###############################################################\n"\
					and lines[index] != "END\n":
					count+=1
print count

