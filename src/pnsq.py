import nsq
import tornado.ioloop
import time
import threading

def pub_message():
    writer.pub('test', b'test', finish_pub)

def finish_pub(conn, data):
    print(data)

# writer = nsq.AsyncConn('127.0.0.1',4150)

writer = nsq.Writer(['192.168.10.251:6000'])
tornado.ioloop.PeriodicCallback(pub_message, 1000).start()

writer.connect()

# async def tt():
#     nsq.run()

# def run(coroutine):
#     try:
#         coroutine.send(None)
#     except StopIteration as e:
#         return e.value

# run(tt())

# def handle_client():
#     nsq.run()

# thread = threading.Thread(target=handle_client)
# thread.start()

