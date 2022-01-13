from prototype import primitives
import random

#######
# Fuzz Generators
#######

class FuzzGenerator:
    pass


class RandomGenerator(FuzzGenerator):
    pass


class RandIntGenerator(RandomGenerator):
    def random_int8(self):
        return primitives.Int8.rand

    def random_int16(self):
        return primitives.Int16.rand

    def random_int32(self):
        return primitives.Int32.rand

    def random_int64(self):
        return primitives.Int64.rand


class RandUintGenerator(RandomGenerator):
    def random_uint8(self):
        return primitives.Uint8.rand

    def random_uint16(self):
        return primitives.Uint16.rand

    def random_uint32(self):
        return primitives.Uint32.rand

    def random_uint64(self):
        return primitives.Uint64.rand


class RandStringGenerator(RandomGenerator):
    def random(self, max=4096):
        length = random.randint(1, max)
        return ''.join(chr(random.randint(0,255)) for _ in range(length))

    def get_chr(self):
        return ''.join(chr(random.randint(0,255)) for _ in range(1))

    def get_str(self, length=None):
        if length == None:
            length = random.randint(1, 4096)
        return ''.join(chr(random.randint(0,255)) for _ in range(length))