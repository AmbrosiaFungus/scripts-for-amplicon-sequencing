#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:40:15 2017

@author: robert
"""

import os
import shutil
import csv

data_dir = "Here comes the path to the directory where your fastq.gz files are"
with open (r'phred64_Bacteria.csv',"w") as f: #Name of the manifest file
    writer = csv.writer(f)
    writer.writerow(["sample-id","absolute-filepath","direction"])

    x = os.listdir(data_dir)
    #print(x)
    for filename in x:
        if filename.startswith('RM'): # our sequencing facility gives us a fastq.gz file starting with an identifier, in this case my initials "RM"
            myarray = filename.split('_')
            sample_nb = myarray[0]
            if myarray[3] == "R1": #specify the forward reads
                direction="forward"
            else:
                direction="reverse"
            filepath = (os.path.join(data_dir, filename))
            writer.writerow([sample_nb, filepath, direction])
