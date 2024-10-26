# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:02:31 2022

@author: GongKe
"""

import sys
import fileinput

#print(sys.argv[0])
#print(sys.argv[1])
#print(sys.argv[2])
water_number = 0
#file_name = sys.argv[1]
file_name = 'SWDP2.data'
with open(file_name,'r') as f:
    with open('newfile1.data','w') as p:
        lines = f.readlines()
        length = len(lines)
        for i in range(length):
            line = lines[i].split()
            if line == []:
                continue
            elif i == 3:
                old_bond_number = line[0]
            elif i == 9:
                old_bond_types = line[0] 
            elif i == 8:
                pair_type = int(line[0])
            elif len(line) > 6 and line[-1] == 'o*' and line[2] == '1':
                water_number += 1
            else:
                continue
        
        bond_types = int(old_bond_types) + 1
        bond_number = int(old_bond_number) + int(water_number)
        c = 1
        list_count = ['o*','h*','M']
        pair_id_list = range(28,28+pair_type+2)
        for i in range(length):
            line = lines[i].split()
            
            if i == 3:
               p.write('   ')
               line[0] = bond_number
               p.write(str(line[0]) + ' ')
               p.write(str(line[1]) + '\n')
               
            elif i == 9:
                p.write('   ')
                line[0] = bond_types
                p.write(str(line[0]) + ' ')
                p.write(str(line[1]) + ' ')
                p.write(str(line[2]) + '\n')
            
            elif i in pair_id_list:
                pass
            
            
            elif len(line)==5 and line[0] ==old_bond_types:
                p.write(lines[i])
                
                line_bond_coff = lines[i-int(old_bond_types)-1].split()
                if line_bond_coff[0] == 'Bond' and line_bond_coff[1] == 'Coeffs':
                    p.write('   ')
                    line[0] = bond_types
                    p.write(str(line[0]) + '    ')
                    p.write(str('500.0  0.240340') + '\n')
                else:
                    pass
                
            elif  len(line) == 4 and line[0] == old_bond_number:
                
                p.write(str(lines[i]))
                a = 1
                b = 4
                for j in range(1,int(water_number)+1):
                    p.write('  ')
                    p.write(str(int(old_bond_number)+j) + '   ')
                    p.write(str(bond_types) + '   ')
                    p.write(str(a) + '   ')
                    p.write(str(b) + '\n')
                    a += 4
                    b += 4
                    
            elif len(line) == 12 and line[11] in list_count:
                print(line)
                line[1] = c
                p.write('   ')
                p.write(str(line[0]) + '      ')
                p.write(str(line[1]) + '   ')
                p.write(str(line[2]) + '  ')
                p.write(str(line[3]) + '    ')
                p.write(str(line[4]) + '    ')
                p.write(str(line[5]) + '    ')
                p.write(str(line[6]) + '   ')
                p.write(str(line[7]) + '   ')
                p.write(str(line[8]) + '   ')
                p.write(str(line[9]) + ' ')
                p.write(str(line[10]) + ' ')
                p.write(str(line[11]) + '\n')
                if line[11] == 'M':
                    c+=1
                else:
                    pass
                
            
            else:
                p.write(lines[i])
                
    p.close()    
f.close()
print(water_number)
print(old_bond_number)
print(old_bond_types)

content = open('newfile1.data')
with open('Change_polar_name.data','w') as f:    
    for line in content:
        f.write(line.replace('o*', 'ODw').replace('h*', 'Hw'))
f.close()