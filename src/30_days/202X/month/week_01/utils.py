import timeit
import os
import psutil


def timer(func):
    def wrapper():
        start = timeit.default_timer()
        func()
        stop = timeit.default_timer()
        print(f'Run time: {stop - start}')

    return wrapper


def memory_usage(func):
    def wrapper():
        func()
        process = psutil.Process(os.getpid())
        memory = process.memory_info().rss / (1024 * 1024)
        print(f'Memory usage: {memory}MB')

    return wrapper
