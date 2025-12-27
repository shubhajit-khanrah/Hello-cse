import threading
import queue
import time
msg_queue = queue.Queue()
def publisher():
    messages = ['Hai', 'Hello', 'Everyone']
    for msg in messages:
        print(f"Publishing: {msg}")
        msg_queue.put(msg)
        time.sleep(1)
def subscriber(name):
    while True:
        msg = msg_queue.get()
        print(f"{name} received: {msg}")
        msg_queue.task_done()
sub1 = threading.Thread(target=subscriber, args=('Subscriber 1',))
sub2 = threading.Thread(target=subscriber, args=('Subscriber 2',))
sub1.daemon = True
sub2.daemon = True
sub1.start()
sub2.start()
publisher()
msg_queue.join()
