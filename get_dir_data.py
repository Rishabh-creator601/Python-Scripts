import os,glob,sys
import numpy as np



# path = "C:\\logs\\Godown\\Mastering-OpenCV-4-with-Python\\"



def check_dir(path):
	if os.path.exists(path):
		return True
	else:
		return False

def count_details(path):
	

	n_folders  = 0
	n_files  = 0

	all_files = []
	roots  = []
	exts  = {"No Ext":0}


	for root,dirs,files in os.walk(path):




		roots.append(root)


		for dir_ in dirs:
			n_folders += 1



		for file in files:

			n_files  +=  1
			ext = file.split(".")

			if len(ext) >= 2:
				ext = ext[1]

			if len(ext) < 2:
				ext = 'No Ext'
				


			if not ext in exts.keys():
				exts[ext] = 0

			if ext in exts.keys():
				exts[ext] += 1

			all_files.append(ext)



	return (n_folders,n_files,all_files,roots,exts)



    


# n_folders,n_files,all_files,roots,exts = count_details(path)




