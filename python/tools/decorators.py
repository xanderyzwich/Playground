from time import time


def function_logger(func):
    def wrapper_function_logger(*args, **kwargs):
        has_args, has_kwargs = len(args) > 0, len(kwargs) > 0

        announce = f'Calling {func.__name__}()' \
                   + (' with' if any([has_args, has_kwargs]) else '')\
                   + (f' args: {args}' if has_args else '')\
                   + (' and' if all([has_args, has_kwargs]) else '')\
                   + (f' kwargs: {kwargs}' if has_kwargs else '')
        print(announce, end=' - ')

        output = func(*args, **kwargs)
        print(f'returning "{output}"')
        return output

    return wrapper_function_logger


def has_elements(list):
    return len(list) > 0


def print_optional(print_str, control_bool):
    if control_bool:
        print(print_str)


def print_function_call(func, args, kwargs, indent='  '):
    print(f'\nCalling {func.__name__}()')
    print_optional(f'{indent}Args:   {args}', has_elements(args))
    print_optional(f'{indent}Kwargs: {kwargs}', has_elements(kwargs))


def function_details(func, concurrent=False):
    indent = '  '

    def wrapper_function_details(*args, **kwargs):
        if not concurrent:
            print_function_call(func, args, kwargs, indent)

        start = time()
        output = func(*args, **kwargs)
        end = time()

        if concurrent:
            print_function_call(func, args, kwargs, indent)

        print(f'{indent}Return: {output}')
        print(f'{indent}Runtime: {int((end-start) * 1000)} millis')
        return output

    return wrapper_function_details


def function_details_concurrent(func):
    return function_details(func, concurrent=True)

