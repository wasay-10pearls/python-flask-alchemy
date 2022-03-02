import functools
from os import access
import re


user = {"username": "jose", "access_level": "admina"}



def getSecure(level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            print (**kwargs)
            if user["access_level"] == level:
                return func(*args, **kwargs)
            else:
                return f"no access"
        print("step1")
        return secure_function
    return decorator

@getSecure("admin")
def get_admin_password():
     return "abdcd"


print(get_admin_password())