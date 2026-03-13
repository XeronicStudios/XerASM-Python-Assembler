import ctypes as c
import os
_file = 'libtest.lib'
_path = os.path.join(*(os.path.split(__file__)[:-1] + (_file, )))
_mod = c.cdll.LoadLibrary(_path)

test = _mod.testcall
test.restype = c.c_int

print(test(2))
print("Test")