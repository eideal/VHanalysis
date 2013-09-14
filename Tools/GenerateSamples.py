#!/usr/bin/python

import os
import glob
import sys
from Sample import Sample

#PathToFiles = '/afs/cern.ch/user/i/ideal/eos/atlas/atlascerngroupdisk/phys-higgs/HSG4/VHtautau/commonNtuple/VHCNv00-05/'
PathToFiles = '/afs/cern.ch/work/i/ideal/VHCNv00-05/'
#PathToFiles = '/group/atlas/data/D3PD/ideal/VH/CommonNtuples/'
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
    #if BG == 'Z+VBF': continue
    #if BG == 'Z+TVBF': continue

    ## directory-wise naming rules
    suffix = ''
    if (('W+Jets' in BG) and not ('W+Jets' == BG)) or \
      (('Top' in BG) and not ('Top' == BG)) or \
      (('Z+Jets' in BG) and not ('Z+Jets' == BG or 'DYZ+Jets' == BG)):
        suffix = '_' + BG.split('_')[-1]
    
    dirslist = os.listdir(PathToFiles+BG) #dirslist contains indiv files
    for sample in dirslist:    #loop over samples in dirslist
        part = sample.split('.') #split the sample name
        if part[0] in lines: continue
        
        #print '    ', part[0]     #print the first part of sample name
        #print '   ', PathToFiles + BG + '/' + sample
 
        #print '%s,' % part[0]

        ## sample-wise naming rules
        prefix = ''
        if BG == 'Z+VBF':
            if not part[0].startswith('VBF_'):
                prefix = 'VBF_'
            part[0] = part[0].replace('_ATau', '')

        if BG == 'Z+TVBF':
            part[0] = part[0].replace('_ATau', '')
        
        sampleName = prefix + part[0] + suffix
        samplePath = PathToFiles + BG + '/' + sample
        output.write(sampleName + ' = Sample(\n')
        output.write(tab + 'name = \'' + sampleName + '\',\n')
        output.write(tab + 'path = \'' + samplePath  + '\')\n')
        output.write('\n')
        print '    ', sampleName
        
output.close()

