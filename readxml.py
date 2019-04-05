# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 18:31:47 2019

@author: home
"""

import xml.etree.ElementTree as ET
root = ET.parse('000001.xml').getroot()
#rect=[]
#for type_tag in root.findall('object/bndbox'):#/bndbox'):
#    print(type_tag.tag)
#    candidates =[]
#    for item in type_tag:
#        print(item.tag, end=" ")
#        print(item.text)
#        rect.append(item.text)
#    candidates.append(rect)

originalboxes=[]             #list of all [xmin, ymin, xmax, ymax]
for type_tag in root.findall('object/bndbox'):#/bndbox'):
    print(type_tag.tag)
    rect=[]               #rect contains the 4 coordinates of one particular bounding box
    for item in type_tag:
        print(item.tag, end=" ")
        print(item.text)
        rect.append(item.text)
    originalboxes.append(rect)
for i in originalboxes:
    print(i)
        
        
#overlap= abs((min(r1.x, r2.x) - max(l1.x, l2.x)) *  (min(r1.y, r2.y) - max(l1.y, l2.y))) 
