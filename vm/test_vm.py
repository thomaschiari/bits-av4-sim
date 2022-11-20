#!/usr/bin/env python3

#!/usr/bin/env python3

from myhdl import bin
from bits import vm_test
import os.path
import math

SP = 0
STACK = 256
TEMP = {0: 5, 1: 6, 2: 7, 3:8, 4:9, 5:10, 6:11, 7:12}

def init_ram():
    ram = {0: 256}
    return ram

def test_abs_positivo():
    ram = init_ram()
    ram[TEMP[0]] = 6
    tst = {TEMP[0]:6}
    assert vm_test(os.path.join("vm", "abs"), ram, tst)

def test_abs_negativo():
    ram = init_ram()
    ram[TEMP[0]] = -2
    tst = {TEMP[0]:2}
    assert vm_test(os.path.join("vm", "abs"), ram, tst)

def test_fact_zero():
    ram = init_ram()
    ram[TEMP[0]] = 0
    tst = {TEMP[0]:1}
    assert vm_test(os.path.join("vm", "fact"), ram, tst)

def test_fact_one():
    ram = init_ram()
    ram[TEMP[0]] = 1
    tst = {TEMP[0]:1}
    assert vm_test(os.path.join("vm", "fact"), ram, tst)

def test_fact_three():
    ram = init_ram()
    x = 3
    ram[TEMP[0]] = x
    tst = {TEMP[0]:math.factorial(x)}
    assert vm_test(os.path.join("vm", "fact"), ram, tst)

def test_fact_generic():
    ram = init_ram()
    x = 6
    ram[TEMP[0]] = x
    tst = {TEMP[0]:math.factorial(x)}
    assert vm_test(os.path.join("vm", "fact"), ram, tst)
