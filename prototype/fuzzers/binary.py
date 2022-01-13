from prototype.fuzzers.generic import GenericBinaryFuzzer

class CmdlineArgFuzzer(GenericBinaryFuzzer):
    def __init__(self, target_bin, args_list) -> None:
        super().__init__(target_bin, args_list=args_list)
    
    def init_test_case(self):
        for idx in range(len(self.args_list)):
            if self.args_list[idx] == "@@":
                self.args_list[idx] = self.current_testcase_data


class EnvFuzzer(GenericBinaryFuzzer):
    def __init__(self, target_bin, args_list, target_var) -> None:
        self.target_var = target_var
        super().__init__(target_bin, args_list=args_list)
    
    def init_test_case(self):
        self.env_copy[self.target_var] = self.current_testcase_data


class FileFuzzer(GenericBinaryFuzzer):
    def __init__(self, target_bin, args_list) -> None:
        super().__init__(target_bin, args_list=args_list)
    
    def init_test_case(self, binary_data=False):
        if not self.current_testcase_data:
            raise Exception
        if not self.current_testcase_id:
            self.generate_test_case()
        o_mode = "wb+" if binary_data else "w+"
        with open(self.current_testcase_id, o_mode) as case_file:
            case_file.write(self.current_testcase_data)