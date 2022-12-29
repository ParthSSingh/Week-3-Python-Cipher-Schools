# Generators
# Eager Loading
def generate_squares(n):
    return [ i**2 for i in range(1, n) ]
    # for i in range(1, 100):
    #     a.append(i**2)

    # return a

# for x in a:
#     print(x)
for x in generate_squares(100):
    print(x)
# Keyword: 'yield'
from time import sleep
def func():
    print("started")
    yield
    # for i in generate_squares(1000000000000000):
    #     pass
    sleep(5)
    print("ended")
    print("hello")
it = iter(func())
next(it)
print("world")
next(it)print("hello")
def func():
    print("start")
    yield 1
    print("yielded 1")
    yield 2
    print("yielded 2")
it = iter(func())
next(it)
next(it)
# Lazy Loading
def generate_squares(n):
    for i in range(1, n):
        yield i**2
a = generate_squares(10)
type(a)
it = iter(generate_squares(10))
next(it)
a = generate_squares(10)
next(a)
for i in generate_squares(10):
    print(i)
a = ( i**2 for i in range (10) )
# type(a)
for i in a:
    print(i)
for i in a:
    print(i)
a = (i**2 for i in range(10))
iter(a)
a
next(a)
next(a)
for i in a:
    print(i)