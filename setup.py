
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:08:30 2021

@author: map
"""

from config import *
simple_cmd_command(f"pip3 install sklearn")
simple_cmd_command(f"git clone https://github.com/huggingface/transformers")
simple_cmd_command(f"mkdir {models_path}/")
simple_cmd_command(f"cd transformers && git checkout tags/v4.9.1")
simple_cmd_command(f"cd transformers && pip3 install . && python setup.py install")
simple_cmd_command(f"pip3 install -r transformers/examples/pytorch/_tests_requirements.txt")
