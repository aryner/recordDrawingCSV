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
files = []
for dirname, dirnames, filenames in os.walk(directory):
  files = filenames

for f in files:
  if hasCSVExt(f):
    csvFile = '%s%s'%(directory,f)
    imgFile = '%s%s%s'%(directory,f[:-3],'jpg')
    points = []
    with open(csvFile, 'rb') as csvfile:
      reader = csv.reader(csvfile,delimiter=' ', quotechar='|')
      for row in reader:
        if row[0] != 'x,':
          point = (int(row[0].translate(None,''.join([',',' ']))),int(row[1]))
          print point[0]
          points.append(point)
      img = cv2.imread(imgFile)
      for point in points:
        cv2.circle(img,(point[0],point[1]),2,(255,0,0),-1)
      cv2.namedWindow('image')
      cv2.imshow('image',img)
      while(1):
        key = cv2.waitKey(20) & 0xFF
        if key == 27:
          break
      cv2.destroyAllWindows()
