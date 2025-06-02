from fnmatch import fnmatch,fnmatchcase
from helper import sample_paths as paths 
import os 

files = os.listdir(paths[0]) # just path of random directory 


'''
 
kind of lies b/w strings and regular expressions

fnmatch : - case sensitive and has pattern matching such as 

*.txt and *.TXT are treated differently 

*.ext  -> filename.extension
[seq].ext  ->  a specific patten.extension
?.ext ->  any single char.extension


fnmatchcase(filename,regexp})

other functions :

translate 
filter 



other alternatives can be endwith and startswith function 

'''
txt_files= []
for i  in files:
    if fnmatch(i,"*.txt"):
        txt_files.append(i)
    

print(txt_files)