import os, sys
path = "."
dirs = os.listdir( path )
total_thread = 0
write_to_filename = "intergratedThreads.txt"
with open(write_to_filename, "a") as w:
	for filename in dirs:
		if filename == "Readme" or filename == "count_thread.py" or filename == \
		write_to_filename or filename == "intergrate.py" or filename == ".DS_Store"\
		or filename == "t.txt" :
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