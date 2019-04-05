# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 20:53:16 2019

@author: home
"""
#from ipm import mynewlist
import ipm
import readxml
import matplotlib.pyplot as plt
print(readxml.originalboxes)
Th=(0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0)
Precision=[]
Recall=[]
#print(ipm.mynewlist)
#threshold=0.5
for x in range(len(Th)):
    threshold=Th[x]
    lis=[[0, 191, 169, 374],      # [xmin, ymin, xmax, ymax]
         [153, 55, 335, 232],
         [0, 191, 170, 374],
         [155, 74, 335, 232],
         [339, 23, 499, 159],
         [348, 85, 499, 224],
         [163, 0, 499, 374],
         [0, 0, 335, 313],
         [339, 22, 499, 159],
         [0, 191, 189, 374]]
    count_TP=0
    #count_FN=
    val=0.0
    dict={}

    #append each entry in lis to make[xmin,ymin,xmax,ymax,iou] with iou=0
    for j in lis:
        j.append(0)
    
    #update the value of iou for every overlap of detected box with original box    
    for i in readxml.originalboxes:
        #count_TP=0
        j[4]=0
        temp=i
        dict[tuple(temp)]=[]
        #i.append(0)
        for j in lis:
        
            intersect=abs((min(float(i[2]),j[2])-max(float(i[0]),j[0])) * (min(float(i[3]),j[3])-max(float(i[1]),j[1])))
            #print(intersect)
            union=(abs(float(i[2])-float(i[0]))*abs(float(i[3])-float(i[1]))) + (abs(j[2]-j[0]) * abs(j[3]-j[1])) - intersect
            iou=intersect/union
            print("iou", end=" ")
            print(iou)
            #print(iou)
            #if iou>=0.5:
            #val=(max(float(i[4]),iou))
                #if val==iou and i[4]==0:
                #    count_TP+=1
                
                #i[4]=val
            j[4]=iou
            #print("inloop")
            #print(j)
            print("printing tuple",end=" ")
            print(tuple(temp))
            #print(dict[tuple(temp)])
            (dict[tuple(temp)]).append(j)       #****error*****
                
            print(dict[tuple(temp)])
            print("\n")
                #temp=tuple(i)
                #dict[i].append(tuple(j))
    print("printing dictionary")
    for i in dict:
        print(i,dict[i])
        print("\n")
                    
    for i in dict:
        maximum_iou=0
        for j in dict[i]:
            maximum_iou=max(j[4], maximum_iou)
            if maximum_iou>threshold:
                count_TP+=1
        print("maximum iou ", maximum_iou)
    
    print(count_TP)
    #print(count_FN)
 
    print("original boxes")
    for i in readxml.originalboxes:
        print(i)
    
    print("detected boxes")
    for i in lis:
        print(i)
      
    recall=float(count_TP/len(readxml.originalboxes))     
    precision=float(count_TP/len(lis))
    print(recall)
    print(precision)
    Recall.append(recall)
    Precision.append(precision)

plt.plot(Th,Precision,color='green')
plt.show()
plt.plot(Th,Recall,color='red')
plt.show()