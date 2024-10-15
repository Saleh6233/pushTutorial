import threading
import time
import numpy as np


def random_integer():
    for i in range(1, 4):
        x = np.random.randint(100, size=(i, 3))
        print(f"Some random integer array: {x}")
        time.sleep(0.5)


def random_float():
    for i in range(1, 4):
        x = np.random.rand(i, 3)
        print(f"Some random float array: {x}")
        time.sleep(0.5)


def random_linspace():
    for i in range(1, 4):
        y = np.linspace(0., 1., i*2).reshape(i, 2)
        print(f"Some linearly spaced array: {y}")
        time.sleep(0.5)


time1 = time.perf_counter()

random_integer()
random_float()
random_linspace()

time2 = time.perf_counter()

print(f"Total time taken = {time2-time1}")


time1 = time.perf_counter()

t1 = threading.Thread(target=random_integer)
t2 = threading.Thread(target=random_float)
t3 = threading.Thread(target=random_linspace)


t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()

print(f"Total time taken = {time2-time1}")
