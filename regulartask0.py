from mycontextmanagers import *


range_size = 10_000_000

with TimeManager() as tm:
    for i in range(range_size):
        i ** 2


with time_manager():
    for i in range(range_size):
        i ** 2
