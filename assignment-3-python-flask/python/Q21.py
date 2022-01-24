from time import time
  
  
def function_timer(func):

    def wrap_func(*args, **kwargs):
        time1 = time()
        result = func(*args, **kwargs)
        time2 = time()
        print(f'Function {func.__name__!r} executed in {(time2 - time1):.4f} sec')
        return result
    return wrap_func
  
  
@function_timer
def timer_check(n):
    for i in range(n):
        for j in range(999):
            (i*j)
  
  
timer_check(5)