# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1

# for i in countdown(10):
#     print(i)
# countdown(10)

# def finder(x):
#     while True:
#         input_text = yield
#         if x in input_text:
#             print(input_text)

# def yielder(source):
#     yield from source

import asyncio

async def greet(name):
    return 'Hello ' + name

# def run(coroutine):
#     try:
#         coroutine.send(None)
#     except StopIteration as e:
#         return e.value

# async def main():
#     names = ['Alabama', 'Bristol', 'Calgary']
#     for name in names:
#         print(await greet(name))

# async def fib(n):
#     if n < 2:
#         return 1
#     else:
#         return await fib(n-1) + await fib(n-2)

# loop = asyncio.get_event_loop()

# async def greeter(name):
#     print("Hi", name, "here")

# try:
#     print("coroutine start")
#     coro = greeter('LP')
#     print('entering event loop')
#     loop.run_until_complete(coro)
# finally:
#     print('closing vent loop')
#     loop.close()

# class A:
#     async def instance_method(self):
#         print('instance method')
#     @classmethod
#     async def class_method(cls):
#         print('class method')
#     @staticmethod
#     async def static_method():
#         print('static method')
# a = A()
# a.instance_method()