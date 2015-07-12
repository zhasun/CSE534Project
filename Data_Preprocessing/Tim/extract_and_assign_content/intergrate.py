import os, sys
path = "."
dirs = os.listdir( path )
total_thread = 0
with open("intergratedThreads.txt", "w") as w:
	for filename in dirs:
		if filename == "Readme" or filename == "count_thread.py" or filename == \
		"intergratedThreads.txt" or filename == "intergrate.py" or filename == ".DS_Store" :
			continue
		with open(filename, "r") as f:
			lines = f.readlines()
			for line in lines:
				w.write(line)
			w.write("\n")
		print("Read "+filename+"")
		f.close()
w.close()
print("\nThreads have been intergrated to intergratedThreads.txt\n")