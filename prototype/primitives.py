#!/usr/bin/env python3
# Definitions of primitive types to be used for constructing
# higher level structures during the creation of a new FuzzTarget class
import random
from prototype.magic import MAGIC_LENGTHS, MAGIC_NUMS

# Primitive base class
class PrimitiveBase():
    def __init__(self):
        self.type_name = ""
        self.type = None

# Numeric Primitives
class NumericPrimitiveBase(PrimitiveBase):
    """Base class for numeric primitives"""
    def __init__(self):
        self.type_name = "_NumericPrimitive_"
        self.type_obj = type(0x0)
    
    @property
    def type(self):
        return self.type_name

    def minus_one(self, num):
        return num - 1

    def plus_one(self, num):
        return num + 1

class IntPrimitives(NumericPrimitiveBase):
    """Base class for Int primitives"""
    def __init__(self):
        self.name = "Int"
    # min
    INT8_MIN    = -(0xff >> 1)
    INT16_MIN   = -(0xffff >> 1)
    INT32_MIN   = -(0xffffffff >> 1)
    INT64_MIN   = -(0xfffffffffffffff >> 1)
    MIN_ALL     = [INT8_MIN, INT16_MIN, INT32_MIN, INT64_MIN]
    # max
    INT8_MAX    = (0xff >> 1)
    INT16_MAX   = (0xffff >> 1)
    INT32_MAX   = (0xffffffff >> 1)
    INT64_MAX   = (0xfffffffffffffff >> 1)
    MAX_ALL     = [INT8_MAX, INT16_MAX, INT32_MAX, INT64_MAX]

class UintPrimitives(NumericPrimitiveBase):
    """Base class for UInt primitives"""
    def __init__(self):
        self.type_name = "Uint"    
    #min
    UINT_MIN    = 0x0

    #max
    UINT8_MAX   = 0xff
    UINT16_MAX  = 0xffff
    UINT32_MAX  = 0xffffffff
    UINT64_MAX  = 0xfffffffffffffff
    MAX_ALL     = [UINT8_MAX, UINT16_MAX, UINT32_MAX, UINT64_MAX]

    @property
    def min(self):
        return self.UINT_MIN
    
    def max_all(self):
        return [UintPrimitives.UINT64_MAX]

class Uint8(UintPrimitives):
    @property
    def max(self):
        return self.UINT8_MAX
    
    @property
    def rand(self):
        return random.randint(self.min, self.max)

class Uint16(UintPrimitives):
    @property
    def max(self):
        return self.UINT16_MAX

    @property
    def rand(self):
        return random.randint(self.min, self.max)

class Uint32(UintPrimitives):
    @property
    def max(self):
        return self.UINT32_MAX

    @property
    def rand(self):
        return random.randint(self.min, self.max)

class Uint64(UintPrimitives):
    @property
    def max(self):
        return self.UINT64_MAX

    @property
    def rand(self):
        return random.randint(self.min, self.max)

class Int8(IntPrimitives):
    @property
    def max(self):
        return self.INT8_MAX

    @property
    def min(self):
        return self.INT8_MIN

    @property
    def rand(self):
        return random.randint(self.min, self.max)

class Int16(IntPrimitives):
    @property
    def max(self):
        return self.INT16_MAX

    @property
    def min(self):
        return self.INT16_MIN

    @property
    def rand(self):
        return random.randint(self.min, self.max)

class Int32(IntPrimitives):
    @property
    def max(self):
        return self.INT32_MAX

    @property
    def min(self):
        return self.INT32_MIN

    @property
    def rand(self):
        return random.randint(self.min, self.max)

class Int64(IntPrimitives):
    @property
    def max(self):
        return self.INT64_MAX

    @property
    def min(self):
        return self.INT64_MIN

    @property
    def rand(self):
        return random.randint(self.min, self.max)


# String Primitives
class String:
    LEN_MULTIPLIERS = MAGIC_LENGTHS
    BASE_STR = "A"

    def __init__(self, data="", target_len=1):
        self.payload = data * target_len

    @property
    def data(self):
        return self.payload

    @classmethod
    def long(data="", mult=2048):
        if not data:
            return String.BASE_STR * mult
        return data * mult    

    def get_all_long(self) -> list():
        return [(self.BASE_STR * m) for m in self.LEN_MULTIPLIERS]

class FmtString(String):
    FMT_P = "%p"
    FMT_N = "%n"
    FMT_X = "%x"
    FMT_IDS = [FMT_P, FMT_N, FMT_X]

    @classmethod
    def fmt_p(mult=1) -> str:
        return FmtString.FMT_P * mult

    @classmethod
    def fmt_x(mult=1) -> str:
        return FmtString.FMT_X * mult

    @classmethod
    def fmt_n(mult=1) -> str:
        return FmtString.FMT_N * mult

    @classmethod
    def get_all(length=10) -> list():
        # divide len/2 to get correct final length since fmt ids are 2 chars long
        return [(fmt_str * (length/2)) for fmt_str in FmtString.FMT_IDS]
