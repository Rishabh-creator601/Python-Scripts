


def stringTemplate(stringVal):
    
    def formatter(**kwargs):
        if "funcs" in kwargs:
            print(kwargs['funcs'])
                
    
    return formatter



obj  = stringTemplate("hello world")

obj(funcs=['count','done'])