
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:18:30 2021

@author: map
"""

train_file = 'train.txt'
test_file = 'test.txt'
models_path = 'models_ckpts'
max_length = 256
model_type = 'gpt2-medium'#'gpt2'#
epochs = 4

import subprocess
def simple_cmd_command(cmd):
    try:
        popen = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, universal_newlines=True)
        for stdout_line in iter(popen.stdout.readline, ""):
            print(stdout_line.rstrip()) 
        popen.stdout.close()
        return_code = popen.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, cmd)
    except:
        print(f"fail to transparent execution::\n\t command = {cmd}")
        subprocess.run(cmd, shell = True)
