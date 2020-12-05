
from tornado.tcpclient import TCPClient
from tornado.ioloop import IOLoop
from tornado.iostream import IOStream
from tornado.iostream import StreamClosedError
import asyncio
import struct
import msgpack
import threading

# class A:
#     async def instance_method(self):
#         print('instance method')
#     @classmethod
#     async def class_method(cls):
#         print('class method')
#     @staticmethod
#     async def static_method():
#         print('static method')

class EchoClient():
    async def connect(self):
        stream = await TCPClient().connect('127.0.0.1', 8000)        
        self.__stream = stream
        self.send_msg(111)
        while True:
            try:
                buf = await stream.read_bytes(2)
                size = self.__handle_head(buf)
                buf = await stream.read_bytes(size)
                data = self.__handle_body(buf)
                print(data)
                await stream.write(buf)
            except StreamClosedError:
                # logger.exception("tcp error")
                break

    def __handle_head(self, buf):
        size, = struct.unpack('H', buf)
        return size
    
    def __handle_body(self, buf):
        data = msgpack.unpackb(buf)
        return data
    
    def send_msg(self, msg):
        print('msg: ', msg)
        body = msgpack.packb({'a':1})
        size = len(body)
        head = struct.pack('H', size) 
        # print(1111)
        self.__stream.write(head+body)
        
c = EchoClient()
loop = asyncio.get_event_loop()

def handle_client():
    try:
        coro = c.connect()
        loop.run_until_complete(coro)
        print("ghhgighighighighi")
    finally:
        print('closing vent loop')
        loop.close()

thread = threading.Thread(target=handle_client)
thread.start()

# handle_client()


# async def connect():
#     return await TCPClient().connect('127.0.0.1', 8888)
#     # body = msgpack.packb({'a':1})
#     # size = len(body)
#     # head = struct.pack('H', size) 
#     # await connection.write(head+body)

# def run(coroutine):
#     try:
#         coroutine.send(None)
#     except StopIteration as e:
#         return e.value

# client = run(connect())



# loop = asyncio.get_event_loop()

# try:
#     # print("coroutine start")
#     coro = connect()
#     # print('entering event loop')
#     loop.run_until_complete(coro)
# finally:
#     # print('closing vent loop')
#     loop.close()
