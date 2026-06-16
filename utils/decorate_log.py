# that decorate scene of program logs
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print('-+-' * 50)
        func(*args, **kwargs)
        print('-+-' * 50)

    return wrapper