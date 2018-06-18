#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:40:15 2017

@author: robert
"""

import os
import csv



user_input = str(input("Enter the path where you stored your .fastq files: "))

#check if the directory exists

try:
    os.listdir(user_input)
    print("Directory exists")
except:
    print("This directory does not exist")


# check if the specified filepath has .fastq files
counter = 0
for file in os.listdir(user_input):
    if file.endswith('.fastq.gz'):
        counter+=1

if counter ==0:
    print("This directory does not contain .fastq files, try again")
else:
    print("Valid .fastq files found")


    user_input_names = input("Enter the initials of your .fastq files: ") # our sequencing facility gives us a fastq.gz file starting with an identifier
    user_input_naming_file =input("What name do you want to give your file, dont forget the ending of .csv: ")



    # check if the specified filepath has .fastq files

    for file in os.listdir(user_input):
        if file.endswith('.fastq.gz'):
            print("Valid .fastq files")
        else:
            print("This directory does not contain .fastq files, try again")



    with open (user_input_naming_file,"w") as k:
        writer = csv.writer(k)
        writer.writerow(["sample-id","absolute-filepath","direction"])

        x = os.listdir(user_input)
        #print(x)
        for filename in x:
            if filename.startswith(user_input_names):
                myarray = filename.split('_')
                sample_nb = myarray[0]
                if myarray[3] == "R1": #specify the forward reads
                    direction="forward"
                else:
                    direction="reverse"
                filepath = (os.path.join(user_input, filename))
                writer.writerow([sample_nb, filepath, direction])
