#!/usr/bin/env python3

import os.path
from myhdl import bin
from bits import nasm_test, createDir
from Code import testCode

SP = 0
STACK = 256
TEMP = {0: 5, 1: 6, 2: 7, 3:8, 4:9, 5:10, 6:11, 7:12}
TRUE = -1
FALSE = False


def abs_path(file):
    dir_test = os.path.dirname(__file__)
    return os.path.join(dir_test, file)

def code_to_nasm(command, nasm):
    createDir(nasm)
    fNasm = open(nasm, "w")
    code = testCode(fNasm)
    code.writeArithmetic(command)

def vm_test(command, ram, test, time=10000):
    nasm = os.path.join("nasm", command + ".nasm")
    code_to_nasm(command, nasm)
    return nasm_test(nasm, ram, test, time)

def test_delete():
    x = 4; y = 8
    ram = {0: 258, 256: x, 257: y}
    tst = {0: 257, 256: x}
    assert vm_test('delete', ram, tst)

def test_swap():
    x = 4; y = 8
    ram = {0: 258, 256: x, 257: y}
    tst = {0: 258, 256: y, 257: x}
    assert vm_test('swap', ram, tst)

def test_add3():
    x = 14; y = 12; z=1
    ram = {0: 259, 256: x, 257: y, 258: z}
    tst = {0: 257, 256: x+y+z}
    assert vm_test('add3', ram, tst)
