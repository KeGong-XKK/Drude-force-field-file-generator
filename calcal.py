# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:59:47 2022

@author: Ke Gong
"""

import sys
import math
import fileinput
import os
import time

filename = sys.argv[1]
generage_file = sys.argv[2]
c3 = str(sys.argv[3])
oh = str(sys.argv[4])
#filename = 'jiachunbox.data'
l_deta = []
l_xita = []

start = time.time()
with open(filename,'r') as f:
    with open('test.data','w') as q:
        
        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i].split()
            if i == 8:
                atom_types = int(line[0])
                
            elif len(line) !=0 and line[0] == 'Pair' and line[1] == 'Coeffs':
                m = i
                break
            else:
                pass
        print('Find atom types is -------> {}'.format(atom_types))    
        for i in range(len(lines)):            
            line = lines[i].split()                            
            if i in list(range(m,m+atom_types+2)):                                
                if len(line)!= 0 and line[0] == 'Pair' and line[1] == 'Coeffs':
                    for bili in range(i+2,i+atom_types+2):
                        line_cal = lines[bili].split()
                        l_deta.append(float(line_cal[1]))
                        l_xita.append(float(line_cal[2]))
                else:
                    pass
            else:
                q.write(str(lines[i]))
        q.close()
f.close()

                                  
content = open('test.data')
with open(generage_file,'w') as f:    
    for line in content:
        f.write(line.replace(c3, 'CTO').replace(oh, 'OH'))
f.close()                


with open('pair_coff.data','w') as f:
    for i in range(len(l_deta)-1):
        deta = math.sqrt(l_deta[i]*l_deta[i])
        xita = math.sqrt(l_xita[i]*l_xita[i])
        f.write(str('pair_coeff') + '    ')
        f.write(str(i+1) + '    ')
        f.write(str(i+1) + '    ')
        f.write(str('lj/cut/coul/long') + '    ')
        f.write(str(deta) + '    ')
        f.write(str(xita) + '\n')
        for j in range(len(l_deta)-i-1):
            deta = math.sqrt(l_deta[i]*l_deta[i+j])
            xita = math.sqrt(l_xita[i]*l_xita[i+j])
            f.write(str('pair_coeff') + '    ')
            f.write(str(i+1) + '    ')
            f.write(str(i+j+2) + '    ')
            f.write(str('lj/cut/coul/long') + '    ')
            f.write(str(deta) + '    ')
            f.write(str(xita) + '\n')
        
f.close()    
os.system('rm -rf test.data')   
end = time.time()
print('Well Done---------------------> Time spend is {} s' .format(round(end-start,2)))    
    


