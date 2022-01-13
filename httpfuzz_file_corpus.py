#!/usr/bin/env python3
import threading
import glob
import sys

from prototype import generator
from prototype.fuzzers.http import RawHttpFuzzer
from prototype.monitoring.httping import ping

monitor_ev = None
TEST_CASE_BUFFER = []

# config
######
RHOST = "192.168.50.1"
PATH = "/"
PORT = "80"
HEADERS = {}
TESTCASE_DIR = ""
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

def add_to_buffer(req):
    global TEST_CASE_BUFFER
    if len(TEST_CASE_BUFFER) == 3:
        new_t = TEST_CASE_BUFFER[2:].append(req)
        TEST_CASE_BUFFER = new_t
    else:
        TEST_CASE_BUFFER.append()

httpfuzzer = RawHttpFuzzer(RHOST, port=PORT, url_path=PATH, headers=HEADERS)
corpus_files = glob.glob(TESTCASE_DIR + "/*")
spawn_monitor_thread()
for file in corpus_files:
    if monitor_ev.is_set():
        print("LOST CONNECTION TO TARGET...did it crash?")
        print("last 3 testcases sent: ")
        for case in TEST_CASE_BUFFER:
            print(case)
        sys.exit(0)
    req = httpfuzzer.parse_from_file(file)
    add_to_buffer(req)
    httpfuzzer.sendtcp(req)