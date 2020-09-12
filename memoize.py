def memoize(func):
    dict_mem = {}
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if(key not in dict_mem):
            dict_mem[key] = func(*args, **kwargs)
        return(dict_mem[key])
    return(memoizer)