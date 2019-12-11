def decorator_x(func):
    def wrapper_func():
        print('X' * 20)
        func()
        print('X' * 20)

    return wrapper_func

@decorator_x
def says_hello():
    print('hello_world')


says_hello()
