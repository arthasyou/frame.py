from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError
from tornado.ioloop import IOLoop
from uuid import uuid4
from loguru import logger
import struct
import msgpack

class EchoServer(TCPServer):
    async def handle_stream(self, stream, address):   
        print("connected")     
        self.__stream = stream
        self.__address = address
        self.__uuid = str(uuid4())
        # logger.debug("stream: {} address: {}", stream, address)
        while True:
            try:
                buf = await stream.read_bytes(2)
                size = self.__handle_head(buf)
                buf = await stream.read_bytes(size)
                data = self.__handle_body(buf)
                print(data)
                buf = self.__back(data)
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
    
    def __back(self, data):
        body = msgpack.packb(data)
        size = len(body)
        head = struct.pack('H', size) 
        return head + body



server = EchoServer()
server.listen(8888)
# IOLoop.current().start()

