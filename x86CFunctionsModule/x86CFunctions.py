import ctypes as c
import os
_file = 'libx86CFunctions.lib'
_path = os.path.join(*(os.path.split(__file__)[:-1] + (_file, )))
_mod = c.cdll.LoadLibrary(_path)

testcall = _mod.testcall
testcall.restype = c.c_int

def Testcall(Val):
    return testcall(Val)