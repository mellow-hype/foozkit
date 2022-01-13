#!/usr/bin/env python3
import threading

from random import randint
from prototype import generator
from prototype.fuzzers.http import RawHttpFuzzer
from prototype.monitoring.httping import ping

monitor_ev = None

# config
######
RHOST = "192.168.50.1"
PATH = "/"
PORT = "80"
HEADERS = {}
#######

strgen = generator.RandStringGenerator()

def spawn_monitor_thread():
    global monitor_ev
    if ping(RHOST) < 1:
        print("[!] error reaching host on test ping!")
    # spawn a Ping monitor in a thread
    monitor_ev = threading.Event()
    monitor_thread = threading.Thread(target=ping, args=(RHOST, monitor_ev))
    monitor_thread.start()

httpfuzzer = RawHttpFuzzer(RHOST, port=8000, url_path="/asdf", headers={"Host": "asdf"})
req = httpfuzzer.parse_from_file("./test/http2.test")
mutated = httpfuzzer.mutate(req)
