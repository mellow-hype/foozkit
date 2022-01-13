#!/usr/bin/env python3
import os
from random import randint
from prototype import generator
from prototype import fuzzers
from prototype import primitives
from io import BytesIO


# config
######
TARGET_VAR = "DISPLAY"
CMD_STR = "xrdb /home/hyper/.Xresources"
CMD_LST = CMD_STR.split(" ")
TARGET_BIN = CMD_LST[0]
ARGS_LST = CMD_LST[1:]
#######

strgen = generator.RandStringGenerator()
envfuzz = fuzzers.binary.EnvFuzzer(TARGET_BIN, ARGS_LST, TARGET_VAR)
envfuzz.current_testcase_id = envfuzz.generate_test_case_id()

# 100 iterations of random fuzzing
for cnt in range(1000):
    envfuzz.env_copy = os.environ.copy()
    envfuzz.current_testcase_data = bytes(strgen.get_str(randint(1, primitives.Uint16.UINT8_MAX)).encode("utf-8"))
    
    print("run #{}: {}".format(cnt, repr(envfuzz.current_testcase_data)))
    envfuzz.init_test_case()
    try:
        envfuzz.run(None)
    except ValueError:
        print("invalid input, skipping")

# test long strings
str_type = primitives.String()
all_long = str_type.get_all_long()
for lstring in all_long:
    envfuzz.env_copy = os.environ.copy()
    envfuzz.current_testcase_data = lstring
    envfuzz.init_test_case()
    envfuzz.run(None)