
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:18:30 2021

@author: map
"""

train_file = 'train.txt'
test_file = 'test.txt'
models_dirname = 'Bible_model_ckpts'
inputs_dirname = 'input_files'

import os
_ROOT = os.path.abspath(os.path.dirname(__file__))
#def get_data(path): return os.path.join(_ROOT, models_dirname)
models_path = os.path.join(_ROOT, models_dirname)
inputs_path = os.path.join(_ROOT, inputs_dirname)

max_length = 128 + 64
model_type = 'gpt2-medium'#'gpt2'#
per_device_train_batch_size = 1
epochs = 2
file_split_size = 2**26

import subprocess
def simple_cmd_command(cmd):
    try:
        popen = subprocess.Popen(cmd.strip().split(), stdout=subprocess.PIPE, universal_newlines=True)
        for stdout_line in iter(popen.stdout.readline, ""):
            print(stdout_line.rstrip()) 
        popen.stdout.close()
        return_code = popen.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, cmd)
    except:
        print(f"fail to transparent execution::\n\t command = {cmd}")
        print(subprocess.run(cmd, shell = True))
        
