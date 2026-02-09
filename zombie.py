import os
import time

pid = os.fork()

if pid == 0:  # Child process
    print(f"Child ({os.getpid()}): started")
    print(f"Child ({os.getpid()}) finished")
else:  # Parent process
    print(f"Parent ({os.getpid()}) started")
    time.sleep(30)
    print(f"Parent ({os.getpid()}) finished")
    

