import os

def ping(host, monitor_event=None):
    cmd = f"/sbin/ping -c 1 {host} &>/dev/null"
    resp = os.system(cmd)
    if resp != 0:
        if monitor_event:
            monitor_event.set()
        else:
            return -1
    
class Ping:
    def __init__(self, host, packets=1) -> None:
        self.ping_bin = "/sbin/ping"
        self.packets = packets
        self.cmd = f"{self.ping_bin} -c {self.packets} {host} &>/dev/null"

    def run(self, monitor_event):
        resp = os.system(self.cmd)
        if resp != 0:
            monitor_event.set()

