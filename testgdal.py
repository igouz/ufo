from osgeo import gdal
import numpy as np

dataset = gdal.Open("G:/demo.tif")
print(dataset.GetDescription())
print(dataset.RasterCount) #波段数

cols = dataset.RasterXSize 
rows = dataset.RasterYSize

xoffset = cols/2
yoffset = rows/2

band = dataset.GetRasterBand(3)
r = band.ReadAsArray(xoffset,yoffset,5000,5000)

band = dataset.GetRasterBand(2)
g = band.ReadAsArray(xoffset,yoffset,5000,5000)

band = dataset.GetRasterBand(1)
b = band.ReadAsArray(xoffset,yoffset,5000,5000)

import cv2
import matplotlib.pyplot as plt 
img2 = cv2.merge([r,g,b])
plt.imshow(img2)
plt.xticks([]),plt.yticks([])
plt.show()

def readTif(fileName):
  merge_img = 0;
  driver = gdal.getDriverByName("GTiff")
  driver.Register()
  dataset = gdal.Open(fileName)
  if dataset == None:
    print(fileName + "打开文件失败")
    return
  im_width = dataset.RasterXSize
  print('im_width:',im_width)
  im_height = dataset.RasterYSize 
  pring("im_height",im_height)
  im_bands = dataset.RasterCount 
  im_geotrans = dataset.GetGeoTransform()
  im_proj = dataset.GetProjection()
  if im_bands == 1:
    band = dataset.GetRasterBand(1)
    im_data = dataset.ReadAsArray(0,0,im_width,im_height)
    cdata = im_data.astype(np.uint8)
    merge_img = cv2.merge([cdata,cdata,cdata])
    cv2.imwrite('E:/a.jpg',merge_img)
  elif im_data == 4:
    data1=band1.ReadAsArray(0,0,im_width,im_height).astype(np.uint16)
    data2=band2.ReadAsArray(0,0,im_width,im_height).astype(np.uint16)
    data3=band3.ReadAsArray(0,0,im_width,im_height).astype(np.uint16)
    data4=band4.ReadAsArray(0,0,im_width,im_height).astype(np.uint16)
    merge_img1 = cv2.merge([output3,output2,output1])
    cv2.imwrite('E:/b.jpg', merge_img1)

