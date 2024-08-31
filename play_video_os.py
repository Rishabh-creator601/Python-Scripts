import os 



def play_video(path,name):
	os.system(""" cd {} && "{}" """.format(path,name))
	


