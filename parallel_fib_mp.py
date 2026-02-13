import time
import multiprocessing
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def worker(n):
    result = fib(n)
    print(f"fib({n}) = {result}")

if __name__ == '__main__':
    list = [35, 36, 37, 38, 39]

    pros = []

    start_time = time.time()

    for num in list:
        p = multiprocessing.Process(target=worker, args=(num,))
        pros.append(p)
        p.start()

    for p in pros:
        p.join()
    
    end = time.time()
    print(f"Total time: {end-start_time:.2f} seconds")