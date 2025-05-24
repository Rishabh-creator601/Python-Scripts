import os,shutil,glob 



def copy_items(main_path,folder,from_folders=[],length=0.8):
    
    if not os.path.exists("{}/{}/".format(main_path,folder)):
        os.mkdir(f"{main_path}/{folder}/")
    
    for i in from_folders:
        i = f"{main_path}/{i}"
        files = glob.glob("{}/*".format(i))
        length = int(len(files) * length) 
        files = files[:length]
        
        for j in files:
            shutil.copy(j,f"{main_path}/{folder}/")
        
        print("Folder Name : {} Length Copied : {} ".format(i,length))





#copy_items(main_path="C:\logs\datasets\\rps",folder="test",from_folders=['rock',"paper","scissors"],length=0.2)