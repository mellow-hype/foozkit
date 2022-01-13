import subprocess
import os
import requests

# Fuzzer Classes
class GenericFuzzer:
    def __init__(self) -> None:
        self.current_testcase_id = None

    @staticmethod
    def generate_test_case_id():
        """
        Generate a unique test case ID
        """
        # TODO: replace TEST string with uuid
        return "FUZZ_CASE_" + "TEST"

    def generate_test_case(self):
        """
        Generate a testcase
        """
        raise NotImplementedError

    def init_test_case(self):
        """
        Put the generated testcase wherever it needs to be to
        make it available to the target
        """
        raise NotImplementedError

    def run(self):
        """
        Execute the operation with the given testcase
        """
        raise NotImplementedError

class GenericBinaryFuzzer(GenericFuzzer):
    def __init__(self, target_bin, args_list=None) -> None:
        super().__init__()
        self.target_bin = target_bin
        self.args_list  = args_list
        self.env_copy = os.environ.copy()
        self.current_testcase_data = None

    def run(self):
        cmd = [self.target_bin] + self.args_list
        proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, env=self.env_copy)
        stderr = proc.communicate()
        if stderr:
            print(stderr)

class GenericHttpFuzzer(GenericFuzzer):
    def __init__(self, host, port="80", url_path=None, headers={}, https=False) -> None:
        super().__init__()
        self.proto = "http" if not https else "https"
        self.host = host
        self.port  = port
        self.headers = headers
        self.uri_path = str(url_path).lstrip("/")
        self.target_url = f"{self.proto}://{self.host}/{self.uri_path}"
        self.current_testcase_data = None

    def get(self):
        resp = requests.get(self.target_url, headers=self.headers)

    def post(self, data=None):
        resp = requests.post(self.target_url, headers=self.headers, data=data)
