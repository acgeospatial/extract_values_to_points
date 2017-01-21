## code adapted from below
### http://gis.stackexchange.com/questions/46893/getting-pixel-value-of-gdal-raster-under-ogr-point-without-numpy

from osgeo import gdal,ogr
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os 

def training_points(raster, shp):
	lsx=[]
	lsy=[]
	lsz=[]
	src_ds=gdal.Open(raster) 
	gt=src_ds.GetGeoTransform()
	rb=src_ds.GetRasterBand(1)

	ds=ogr.Open(shp)
	lyr=ds.GetLayer()
	for feat in lyr:
		geom = feat.GetGeometryRef()
		mx,my=geom.GetX(), geom.GetY()  #coord in map units

		#Convert from map to pixel coordinates.
		#Only works for geotransforms with no rotation.
		px = int((mx - gt[0]) / gt[1]) #x pixel
		py = int((my - gt[3]) / gt[5]) #y pixel

		intval=rb.ReadAsArray(px,py,1,1)

		value = float(intval[0]) #### this is the value of the pixel, forcing it to a float
		x = float(mx)
		y = float(my)
		lsz.append(value)
		lsx.append(x)
		lsy.append(y)
		
	return lsx, lsy, lsz

## My points
shp = 'D:/training_extract/fields.shp'
## create a 3dplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
## lable axis
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('reflectance') 
## folder containing my sat data
source = 'D:/training_extract/'
## Using 6 bands so I need 6 colours
colours = ['blue', 'green', 'yellow', 'purple', 'brown', 'orange']
## count to control colours
count = 0
## loop through my source directory
for root, dirs, filenames in os.walk(source):
    for file in filenames:
		## looking for tiles ending with TIF
		if file.endswith('TIF'):
			raster = os.path.join(source, file)
			lsx, lsy, lsz = training_points(raster, shp)
			ax.scatter(lsx, lsy, lsz, s=500, c=colours[count])
			count +=1
## I am cheating a bit here I know that the bands are in this order
plt.legend(["Band 2", "Band 3", "Band 4", "Band 5", "Band 6", "Band 7"])

## show my plot
plt.show()
