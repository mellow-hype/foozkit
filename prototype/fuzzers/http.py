import random
import socket

import requests
from prototype import generator

from prototype.fuzzers.generic import GenericHttpFuzzer

generators = generator.RandStringGenerator()

class HttpFuzzer(GenericHttpFuzzer):
    def __init__(self, host, port="80", url_path=None, headers=..., https=False) -> None:
        super().__init__(host, port=port, url_path=url_path, headers=headers, https=https)

class RawHttpFuzzer(GenericHttpFuzzer):
    def __init__(self, host, port="80", url_path=None, headers=..., https=False) -> None:
        super().__init__(host, port=port, url_path=url_path, headers=headers, https=https)
        self.raw_request = None
        self.raw_response = None

    def sendtcp(self, raw_request=""):
        if not raw_request:
            raw_request = self.raw_request
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, int(self.port)))
            s.sendall(raw_request)
            self.raw_response = s.recv(0x2000)

    def construct_from_template(self, template):
        pass

    def parse_from_file(self, request_file):
        constructed_req = ""
        with open(request_file) as reqfile:
            for line in reqfile:
                fmt_line = line.rstrip() if line != "\r\n" else line
                fmt_line += "\r\n"
                constructed_req += fmt_line
        constructed_req += "\r\n"
        return constructed_req

    def mutate(self, request_data):
        mutated_request = ""

        for line in request_data.split("\n"):
            new_line = str(line).rstrip().replace("@FOOZ@", generators.random())
            new_line += "\r\n"
            mutated_request += new_line
        # print(repr(mutated_request))
        return mutated_request
        # return request_data.replace("@FOOZ@", generators.get_str())
