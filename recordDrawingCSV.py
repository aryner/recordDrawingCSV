import cv2
import os
import sys
import numpy as np

mouseDown = False

def draw(event,x,y,flags,param):
  global mouseDown
  if event == cv2.EVENT_LBUTTONDOWN:
    mouseDown = True
  if event == cv2.EVENT_LBUTTONUP:
    mouseDown = False
  if mouseDown:
    cv2.circle(img,(x,y),2,(255,0,0),-1)

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

for i in range(len(files)):
  if hasImgExt(files[i]):
    img = cv2.imread('%s%s'%(directory,files[i]))
    cont = showImgForDrawing(img)
  else:
    print '%s does not have a jpg extension'%f
