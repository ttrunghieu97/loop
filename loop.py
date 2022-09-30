import os

FJoin = os.path.join 
def GetFiles(path):
	file_list, dir_list = [], []
	for dir, subdirs, files in os.walk(path, topdown=True):
		file_list.extend([FJoin(dir, f) for f in files])
		dir_list.extend([FJoin(dir, d) for d in subdirs])
	file_list = filter(lambda x: not os.path.islink(x), file_list)
	dir_list = filter(lambda x: not os.path.islink(x), dir_list)
	return file_list, dir_list

files, dirs = GetFiles(os.path.expanduser("refinehandpose_left"))
for files in Files:
	# do anything