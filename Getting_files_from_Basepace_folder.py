#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:11:48 2017

@author: robert
"""

import os
import shutil


drs="Here comes the folder where your files are going to"

for file in os.popen('find "Path to the Basespacefolder containing you fastq.gz files" -name \"*fastq.gz"').read().split('\n'):
    shutil.copy(file, drs)
