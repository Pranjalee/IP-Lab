from __future__ import (
    division,
    print_function,
)

#import skimage.data
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import selectivesearch
import cv2
#mynewlist=[]


def main():

    # loading astronaut image
    #img = skimage.data.astronaut()
    img = cv2.imread('000006.jpg')
    #img=Image.open("F:\VOCdevkit\VOC2007\JPEGImages\000008.jpg")
    
    # perform selective search
    img_lbl, regions = selectivesearch.selective_search(
        img, scale=500, sigma=0.9, min_size=10)

    candidates = set()
    for r in regions:
        # excluding same rectangle (with different segments)
        if r['rect'] in candidates:
            continue
        # excluding regions smaller than 2000 pixels
        if r['size'] < 2000:
            continue
        # distorted rects
        x, y, w, h = r['rect']
        if w / h > 1.2 or h / w > 1.2:
            continue
        candidates.add(r['rect'])
        
    mylist=list(candidates)
    #mynewlist=[]
    for i in mylist:
        j=list(i)
        j[2]=j[0]+j[2]
        j[3]=j[1]+j[3]
        #print(j)
        global mynewlist        
        mynewlist.append(j)
    
    for i in mynewlist:
        print(i)
    

    # draw rectangles on the original image
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
    ax.imshow(img)
    cv2.imwrite('result.jpg',img)
    for x, y, w, h in candidates:
        #print(x, y, w, h)
        rect = mpatches.Rectangle((x, y), w, h, fill=False, edgecolor='red', linewidth=1)
        ax.add_patch(rect)

    plt.show()
    #img.close()

if __name__ == "__main__":
    mynewlist=[]
    main()