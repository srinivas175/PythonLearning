## Function based Decorators

# Without args in decorators

import functools

def count_calls(func):
   def wrapper(*args, **kwargs):
      func(*args,**kwargs)
   return wrapper
  
@count_calls
def printName(name):
    print(f'My name is {name}')
   
printName('John')


# with args in decorators
import functools

def call_counts(no_of_iters = 0):
    print('no of iters',no_of_iters)
    def repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for i in range(no_of_iters):
                print(i+1,end=' ')
                func(*args,**kwargs)
        return wrapper
    return repeat

@call_counts(no_of_iters = 10)
def printName(name):
    print(f'My name is {name}')



