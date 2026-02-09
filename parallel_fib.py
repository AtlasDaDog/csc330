import time
import os
start = time.perf_counter()
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

children=[]

list = [35,36,37,38,39]

for i in range(0,5):
    pid = os.fork()

    if pid == 0:
        res = fib(list[i])
        print(f"fib({list[i]}), {res}")
        os._exit(0)
    else:
        children.append(pid)

for _ in children:
    os.wait()



end = time.perf_counter() 

final = end - start

print(f"Total time- {final:.4f} seconds")