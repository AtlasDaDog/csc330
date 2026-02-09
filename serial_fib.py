import time 
start = time.perf_counter() 
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
list = [35,36,37,38,39]

for i in range(0,5):
    g = (fib(list[i]))
    i += 1
    print(g)

end = time.perf_counter()

total = end - start 
print(f"Total Elasped time {total:.4f} secs")