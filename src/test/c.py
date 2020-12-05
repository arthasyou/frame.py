from tornado.tcpclient import TCPClient
from tornado.iostream import StreamClosedError
import tornado.ioloop
import asyncio
import struct
import msgpack

async def main():
    stream = await TCPClient().connect('127.0.0.1', 8888)
    b = packmsg({'a':1})
    await stream.write(b)      
    while True:
        try:
            
            buf = await stream.read_bytes(2)
            size, = struct.unpack('H', buf)
            print(size)
            buf = await stream.read_bytes(size)
            data = msgpack.unpackb(buf)
            print(data)
            bin = packmsg(data)
            await stream.write(bin)
        except StreamClosedError:
            # logger.exception("tcp error")
            break

def packmsg(msg):
    body = msgpack.packb(msg)
    size = len(body)
    head = struct.pack('H', size)
    return head+body

asyncio.run(main())