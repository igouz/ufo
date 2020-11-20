from osgeo import gdal
import numpy as np

merge_img = 0;
fileName = "G:\demo.tif"

dataset = gdal.Open(fileName)
if dataset == None:
  print(fileName + "打开文件失败")
im_width = dataset.RasterXSize
print('im_width:',im_width)
im_height = dataset.RasterYSize 
print("im_height",im_height)
im_bands = dataset.RasterCount 
im_geotrans = dataset.GetGeoTransform()
im_proj = dataset.GetProjection()
if im_bands == 1:
  band = dataset.GetRasterBand(1)
  im_data = dataset.ReadAsArray(0,0,im_width,im_height)
  cdata = im_data.astype(np.uint64)
  merge_img = cv2.merge([cdata,cdata,cdata])
  cv2.imwrite('E:/a.jpg',merge_img)
elif im_bands == 4:
  band1=dataset.GetRasterBand(1)
  band2=dataset.GetRasterBand(2)
  band3=dataset.GetRasterBand(3)
  band4=dataset.GetRasterBand(4)

  data1=band1.ReadAsArray(0,0,im_width,im_height).astype(np.uint64) #r #获取数据
  data2=band2.ReadAsArray(0,0,im_width,im_height).astype(np.uint64) #g #获取数据
  data3=band3.ReadAsArray(0,0,im_width,im_height).astype(np.uint64) #b #获取数据
  data4=band4.ReadAsArray(0,0,im_width,im_height).astype(np.uint64) #R #获取数据
  output1= cv2.convertScaleAbs(data1, alpha=(255.0/65535.0))
  output2= cv2.convertScaleAbs(data2, alpha=(255.0/65535.0))
  output3= cv2.convertScaleAbs(data3, alpha=(255.0/65535.0))
  merge_img1 = cv2.merge([output3,output2,output1]) #B G R
  
  cv2.imwrite('E:/b.jpg', merge_img1)