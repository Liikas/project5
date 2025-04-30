from functools import wraps


def log(filename=None):
    """The decorator automatically records the details of function execution"""
    def my_decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_info = f'{func.__name__} ok'
                if filename:
                    with open(filename, 'a', encoding="utf-8") as text:
                        text.write(log_info)
                        text.write("\n")
                else:
                    print(log_info)
                return result
            except Exception as e:
                log_error = f'{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}'
                if filename:
                    with open(filename, 'a', encoding="utf-8") as text:
                        text.write(log_error)
                        text.write("\n")
                else:
                    print(log_error)
                raise e
        return wrapper

    return my_decor


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
