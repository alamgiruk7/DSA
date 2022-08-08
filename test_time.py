from time import time

def calc_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Program took {(end-start)*1000} milliseconds.")

        return result
    return wrapper