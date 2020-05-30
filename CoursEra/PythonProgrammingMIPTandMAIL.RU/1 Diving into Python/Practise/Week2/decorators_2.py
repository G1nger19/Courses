def logger(filename):
    def decorator(func):
        def wrapped(*args,**kwargs):
            result=func(*args,**kwargs)
            with open(filename,'w') as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator

@logger('log_2.txt')
def summator(num_list):
    return sum(num_list)

print(summator(range(6)))

with open('log_2.txt') as f:
    print(f.read())