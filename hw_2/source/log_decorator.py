from functools import wraps
from datetime import datetime
import time


def function_logger(log_file):
    def decorator(func):
        @wraps(func)
        def wrapper(log_file=None, *args, **kwargs):

            with open(log_file, 'a') as log_file:

                log_file.write(f"{func.__name__}\n")

                start_time = datetime.now()
                log_file.write(f"{start_time}\n")

                log_file.write(f"{args, kwargs}\n")

                result = func(*args, **kwargs)
                log_file.write(f"{result if result is not None else '-'}\n")

                end_time = datetime.now()
                log_file.write(f"{end_time}\n")

                elapsed_time = end_time - start_time
                log_file.write(f"{elapsed_time}\n")

            return result

        return wrapper

    return decorator


@function_logger('test.log')
def greeting_format(name):
    return f'Hello, {name}!'


# greeting_format('test.log')
