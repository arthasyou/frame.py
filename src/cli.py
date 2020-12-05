import socket
import struct
import msgpack
# from tornado.iostream import IOStream
import time
# import tornado
import threading

PORT = 8888
SERVER = "192.168.8.25"
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"



class Cli():
  def __init__(self, host, port):
    self.__host = host
    self.__port = port
  
  def connect(self):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.connect((self.__host, self.__port))
    self.__s = s
    try:
      self.handle_msg()
    except socket.error as e:
      print("socket error: ", e)
      s.close()
    finally:
      print("down")

  
  def handle_msg(self):
    buf = self.__s.recv(2)
    size, = struct.unpack('H', buf)
    buf = self.__s.recv(size)
    data = msgpack.unpackb(buf)
    print(data)
    self.handle_msg()
    
  
  def onClose(self):
    print("socket close")
    
  
  def onConnected(self):
    print("socket connected")
    # self.__stream.read_bytes(8, self.onRead)   
    
  def send(self, msg):
    body = msgpack.packb(msg)
    size = len(body)
    head = struct.pack('H', size)
    self.__s.send(head+body)
  
  def onRead(self):
    print("reading")
    
def handle_client():
    m.connect()

m = Cli("127.0.0.1", 8888)


thread = threading.Thread(target=handle_client)
thread.start()








# def send(msg):
#   body = msgpack.packb(msg)
#   size = len(body)
#   head = struct.pack('H', size) 
#   client.send(head+body)
  

# send({'a':1})

# send(DISCONNECT_MESSAGE)