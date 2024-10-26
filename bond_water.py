# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 19:58:11 2022

@author: GongKe
"""

water_numer = 800

with open('h2o_swdp.data','r') as f:
    with open('new_h2o_sphe.data','w') as p:
        lines = f.readlines()
        length = len(lines)
        for i in range(length):
            line = lines[i].split()
            if i == 3:
               line[0] = water_numer * 2
               p.write('   ')
               p.write(str(line[0]) + ' ')
               p.write(str(line[1]) + '\n')
            elif i == 4:
                line[0] = water_numer
                p.write('   ')
                p.write(str(line[0]) + ' ')
                p.write(str(line[1]) + '\n')
            elif i == 8:
                p.write(str(lines[i]))
                p.write(str('   1 bond types') + '\n')
                p.write(str('   1 angle types') + '\n')
            elif i == 25:
                p.write(str(lines[i]))
                p.write('\n')
                p.write(str('Bond Coeffs') + '\n')
                p.write('\n')
                p.write(str('   1   540.6336     0.9600') + '\n')
                p.write(str('   2   500.0        0.240340') + '\n')
                p.write('\n')
                p.write(str('Angle Coeffs') + '\n')
                p.write('\n')
                p.write(str('   1    37.950526   104.520') + '\n')
                p.write('\n')   
                
                
                
                
            else:
                p.write(str(lines[i]))
        
        p.write(str('Bonds') + '\n')
        p.write('\n')
        
        a = 1
        b = 1
        for i in range(1,water_numer+1):
            for j in range(1,3):
                p.write('     ')
                p.write(str(a) + '   ')
                p.write(str('1') + '     ')
                p.write(str(b) + '     ')
                p.write(str(b+j) + '\n')
                a += 1
            b += 4
        
        p.write('\n')
        p.write(str('Angles') + '\n')
        p.write('\n')
        
        a = 1
        
        for i in range(1,water_numer+1):
            p.write('     ')
            p.write(str(i) + '   ')
            p.write(str('1') + '     ')
            p.write(str(a+1) + '     ')
            p.write(str(a) + '     ')
            p.write(str(a+2) + '\n')
            a += 4
            
            
        
        
        
        
    p.close()
f.close()
            