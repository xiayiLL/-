#Performance Testing 性能测试
import time
import random
from functools import wraps
from arithmetic import integer_score,randomNum,getMedianExpression,newint
  
def fn_timer(function):
  @wraps(function)
  def function_timer(*args, **kwargs):
    t0 = time.time()
    result = function(*args, **kwargs)
    t1 = time.time()
    print ("Total time running : \n%s seconds" %(str(t1-t0)))#function.func_name,
    return result
  return function_timer

@fn_timer
def myfunction(n):
    fh = random.randint(0,3)
    return sorted([newint(fh,2,2) for i in range(n)])
if __name__ == "__main__":
  myfunction(1000000)