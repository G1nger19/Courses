def logger(func):
    def wrapped(num_list):
        result=func(num_list)
        with open('log.txt','w') as f:
            f.write(str(result))
        return result
    return wrapped

@logger
def summator(num_list):
    return sum(num_list)

print(summator(range(6)))

with open('log.txt','r') as f:
    print(f.read())
