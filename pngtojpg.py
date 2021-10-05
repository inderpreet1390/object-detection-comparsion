from glob import glob                                                           
import cv2 
pngs = glob(r'D:\Dataset\New folder\dotacocoHBB\trainval1024\images'+'/*.png')

for j in pngs:
    img = cv2.imread(j)
    cv2.imwrite(j[:-3] + 'jpg', img)