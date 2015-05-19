import cv2
import os
import sys
import numpy as np
import csv

def hasCSVExt(name):
  if '.csv' in name.lower():
    return True
  return False

directory = sys.argv[1]
scale = 1
if len(sys.argv) > 2:
 scale = float(sys.argv[2])
files = []
for dirname, dirnames, filenames in os.walk(directory):
  files = filenames

for f in files:
  if hasCSVExt(f):
    csvFile = '%s%s'%(directory,f)
    imgFile = '%s%s%s'%(directory,f[:-3],'JPG')
    if imgFile not in files:
      imgFile = '%s%s%s'%(directory,f[:-3],'jpg')
    points = []
    with open(csvFile, 'rb') as csvfile:
      reader = csv.reader(csvfile,delimiter=' ', quotechar='|')
      for row in reader:
        if row[0] != 'x,':
          point = (int(row[0].translate(None,''.join([',',' ']))),int(row[1]))
          points.append(point)
      img = cv2.imread(imgFile)
      img = cv2.resize(img,None,fx=scale,fy=scale,interpolation=cv2.INTER_AREA)
      for point in points:
        cv2.circle(img,(int(scale*point[0]),int(scale*point[1])),2,(255,0,0),-1)
      cv2.namedWindow(f)
      cv2.imshow(f,img)
      while(1):
        key = cv2.waitKey(20) & 0xFF
        if key == 27:
          break
      cv2.destroyAllWindows()

