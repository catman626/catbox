import sys
from sys import argv
import os
from os.path import join

if len(argv) != 2 :
    print("usage: python alg-add.py inputfile")
    exit()


inputfile = argv[1] 
algSum = 0
with open(inputfile) as inputf: 
    lines = inputf.readlines()
    lines = [ l for l in lines if l.strip() ]
nums = [ int(l.strip()) for l in lines ]
print(sum(nums))