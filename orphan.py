import os
import time

pid = os.fork()

if pid == 0:  # Child process
    print(f"Child ({os.getpid()}): Working for 30 seconds...")
    time.sleep(30)
    print(f"Child ({os.getpid()}) finished")
else:  # Parent process
    print(f"Parent ({os.getpid()}) started")
    print(f"Parent ({os.getpid()}) finished")

