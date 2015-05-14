import cv2
import os
import sys
import numpy as np

mouseDown = False
csv = None

def draw(event,x,y,flags,param):
  global mouseDown
  global csv
  if event == cv2.EVENT_LBUTTONDOWN:
    mouseDown = True
  if event == cv2.EVENT_LBUTTONUP:
    mouseDown = False
  if mouseDown:
    cv2.circle(img,(x,y),2,(255,0,0),-1)
    csv.write('(%d %d),'%(x,y))

def hasImgExt(name):
  if '.jpg' in name.lower():
    return True
  return False

def showImgForDrawing(img):
  result = True
  cv2.namedWindow('image')
  cv2.setMouseCallback('image',draw)

  while(1):
      cv2.imshow('image',img)
      if cv2.waitKey(20) & 0xFF == 27:
          break
  cv2.destroyAllWindows()
  return result

directory = sys.argv[1]
files = []
for dirname, dirnames, filenames in os.walk(directory):
  files = filenames

for f in files:
  if hasImgExt(f):
    fileName = '%s%s'%(directory,f)
    csv = open('%s%s'%(fileName[:-3],'csv'), 'w')
    img = cv2.imread(fileName)
    cont = showImgForDrawing(img)
    csv.close()
  else:
    print '%s does not have a jpg extension'%f

