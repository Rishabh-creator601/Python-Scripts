import random,string

def random_dict(n_values=5):
    
    keys  = list(string.ascii_lowercase) # just a b c d
    values  = [int(i) for i in list(string.digits)] # just 1 2 3 4
    sample_dict = {}
    
    for i in range(0,n_values):
        sample_dict[keys[i]] =  values[i] +1 
        
    return sample_dict



sample_paths  = ['C:\depository\materials','C:\codes\data']
        
        
