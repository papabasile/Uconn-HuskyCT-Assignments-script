# Ioannis Papavasileiou
# 4/20/2016
# python script to rearrange files downloaded from HuskyCT and sort them by netID on different folders

baseDir = '~/Downloads/projects'

import glob, os
os.chdir(baseDir)
for file in glob.glob('*'):
    splits = file.split('_')
    if len(splits)>=4:
        netID = splits[1]
        filename = splits[-1]
        if not os.path.exists(netID):
            os.mkdir(netID)
        os.rename(file, netID + '/' + filename)
