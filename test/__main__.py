#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import subprocess as cmd
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

def cmd_output(com):
    pipe = cmd.Popen(com, stdout=cmd.PIPE, stderr=cmd.PIPE)
    output, errput = pipe.communicate()
    return output , errput

path_tests = "test/samples"
files = [ f for f in os.listdir(path_tests) if "error" not in f ]


for file in files:
    f = open("%s/%s"%(path_tests, file), "r")
    results = list()
    while "?" is not f.readline()[0]:
        pass
    while 1:
        line = f.readline()
        if not line:
            break
        if line[0] is "#":
            results.append(line[1:].replace(" ", "").rstrip('\n').split('='))
    com = "python expert_system %s/%s"%(path_tests, file)
    output = cmd_output(com.split())
    # if output[1]:
    #     print("\033[91m%s\033[0m"%(output[1]))
    #     sys.exit(0)
    err = 0
    for res in output[0].split('\n')[:-1]:
        split = res.replace(" ", "").split("=")
        if split not in results:
            print("%s ..... \033[93m%s is not in %s\033[0m"%(file, res, results))
            err = 1
    if err is 0:
        print("%s ..... \033[92mOk\033[0m"%(file))
