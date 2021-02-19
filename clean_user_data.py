#!/usr/bin/python3
import os

os.chdir('user_data')
for f in os.listdir():
    os.system('rm ' + f)