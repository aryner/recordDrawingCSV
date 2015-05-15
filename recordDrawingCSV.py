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
    csv.write('%d, %d\n'%(x,y))

def hasImgExt(name):
  if '.jpg' in name.lower():
    return True
  return False

def doesNotHaveCSV(f,files):
  base = f[:-3].lower()
  for ff in files:
    if ff.lower() == '%s%s'%(base,'csv'):
      return False
  return True

def showImgForDrawing(img):
  result = True
  cv2.namedWindow('image')
  cv2.setMouseCallback('image',draw)

  while(1):
    cv2.imshow('image',img)
    key = cv2.waitKey(20) & 0xFF
    if key == 27:
      result = False
      break
    if key == 3:
      result = True
      break
  cv2.destroyAllWindows()
  return result

directory = sys.argv[1]
scale = 1
if len(sys.argv) > 2 :
  scale = float(sys.argv[2])

files = []
for dirname, dirnames, filenames in os.walk(directory):
  files = filenames

for f in files:
  if hasImgExt(f) and doesNotHaveCSV(f,files):
    fileName = '%s%s'%(directory,f)
    csv = open('%s%s'%(fileName[:-3],'csv'), 'w')
    csv.write('x, y\n')
    img = cv2.imread(fileName)
    if scale < 1:
      print 'in if'
      img = cv2.resize(img,None,fx=scale, fy=scale, interpolation = cv2.INTER_AREA)
    cont = showImgForDrawing(img)
    if not cont:
      os.remove('%s%s'%(fileName[:-3],'csv'))
      csv.close()
      break
    csv.close()
  elif hasImgExt(f):
    print '%s already has a csv file'%f
  else:
    print '%s does not have a jpg extension'%f

