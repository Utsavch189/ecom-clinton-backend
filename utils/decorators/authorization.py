from utils.jwt_builder.main import JwtBuilder
from utils.exceptions.main import Unauthorized

def is_authorize(func):
    def wrapper(*args, **kwargs):
        request=args[1]
        if request.META.get('HTTP_AUTHORIZATION'):
            token=request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
            token_data=JwtBuilder(token=token).decode()
            if token_data:
                args[1].token_data=token_data
                return func(*args,**kwargs)
        raise Unauthorized()

    return wrapper
