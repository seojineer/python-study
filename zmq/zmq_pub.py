import zmq
import random
import sys
import time

#port = "12341"
port = 12341
if len(sys.argv) > 1:
    port =  sys.argv[1]
    #port = int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

while True:
    print("[SEOJI] PUB send_multipart(msg) start")
    msg = "hello"
    print("[SEOJI] msg: " + msg)
    socket.send_multipart(msg)
    print("[SEOJI] PUB send_multipart(msg) finish")
    time.sleep(1)
