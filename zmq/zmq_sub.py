import sys
import zmq
from zmq.utils.monitor import recv_monitor_message

#port = "12341"
port = 12341
if len(sys.argv) > 1:
    port =  sys.argv[1]
    #int(port)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
# sub socket option
socket.setsockopt(zmq.SUBSCRIBE, "")

# monitor
monitor = socket.get_monitor_socket(zmq.EVENT_ALL)

print "Collecting updates from zmq_server..."
socket.connect ("tcp://localhost:%s" % port)

while True:
    status = recv_monitor_message(monitor)
    print("[SEOJI] monitor status: " + str(status))

    if status['event'] == zmq.EVENT_CONNECTED:
        print("[SEOJI] EVENT_CONNECTED!")
        break

for i in range(100):
    #msg = socket.recv()
    msg = socket.recv_multipart()
    msg = ''.join(msg)
    print("[SEOJI] recv msg: " + str(msg))
