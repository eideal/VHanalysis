#!/usr/bin/python

import os
import glob
import sys
from Sample import Sample

#PathToFiles = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/lephad/'
PathToFiles = '/group/atlas/data/D3PD/ideal/VH/CommonNtuples/'
dirs = os.listdir(PathToFiles)
#print dirs
f  = open("samples.txt") #files to not include
line = f.readlines()
lines = []
tab = '    '
for raw_line in line:
    lines.append(raw_line.rstrip('\n'))


output = open('Samples.py', 'w')
output.write('from Sample import Sample \n\n')


for BG in dirs: #loop over lephad folders
    print BG
    dirslist = os.listdir(PathToFiles+BG) #dirslist contains indiv files
    for sample in dirslist:    #loop over samples in dirslist
        part = sample.split('.') #split the sample name
        if part[0] in lines: continue
        
        print '    ', part[0]     #print the first part of sample name
        #print '   ', PathToFiles + BG + '/' + sample
 
        #print '%s,' % part[0]

        sampleName = part[0]
        samplePath = PathToFiles + BG + '/' + sample
        output.write(sampleName + ' = Sample(\n')
        output.write(tab + 'name = \'' + sampleName + '\',\n')
        output.write(tab + 'path = \'' + samplePath  + '\')\n')
        output.write('\n')
        #print sampleName
        
output.close()

