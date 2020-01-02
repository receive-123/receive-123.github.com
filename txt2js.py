# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:00:42 2020

@author: 25785
"""

with open('./names.txt', encoding='utf-8') as f:
    names = f.readlines()

txt = []
txt.append('var member = [\n')
for name in names:
    txt.append('    {\n')
    txt.append('        "name": "%s"\n'%name.strip())
    txt.append('    },\n')
txt.append(']\n')
with open('./js/member.txt', 'w', encoding='utf-8') as f:
    f.writelines(txt)