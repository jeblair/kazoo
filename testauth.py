import kazoo.client
import time
import threading
import logging

logging.basicConfig(level=5)
l = logging.getLogger('kazoo')
l.setLevel(5)

client = kazoo.client.KazooClient('localhost:2181')
client.start()

def auth():
    client.add_auth('world', 'anyone')

def test_multi_thread():
    t = threading.Thread(target=auth)
    t.start()
    client.stop()

def test_single_thread():
    try:
        client.add_auth('world', 'anyone')
    except Exception:
        pass
    client.stop()

test_multi_thread()
# test_single_thread()

