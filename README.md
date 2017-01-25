Just how easy is it to extract the values from images? Sentinel 2a is operating with 12 bands; that means every location that is imaged has 12 layers, each measuring 12 different wavelengths. Landsat 8 comprises 11 bands.

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2017/01/spectral.png)

Image from http://landsat.gsfc.nasa.gov/sentinel-2a-launches-our-compliments-our-complements/

In multispectral satellites, such as those described above, there is a huge depth of information. You can read more about the spectral properties in this ‘Introduction to Remote Sensing’article. I wanted to plot some points in QGIS and get the values of the underlying imagery. Being able to do this can help guide the classification of satellite data.

There are such a large variety of ways to extract values from underlying imagery. ArcGIS does this very well with the Spatial Analyst Extension, QGIS has a plugin and there is a question on stackexchange asking how to do this - choose the option that best fits you. However, I wanted to try doing this in a Python script with a view to being able to automate it. Fortunately this can be done using GDAL.

Extracting values from Satellite data(sets) using Python.

In extracting the values from the image my aim is to show the difference between two areas on a multispectral satellite image. I am going to use Landsat 8 bands 2, 3, 4, 5, 6, & 7.

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2017/01/Points_In_raster1.jpeg)

Above is a Landsat 432 RGB image part of the Isle of Wight. The 8 points plotted are point Shapefiles created in QGIS. I haven’t labelled them but 7 are in ‘green’ fields and 1 is in a ‘brown’ or ploughed field. I am going to extract the values for the bands mentioned above and plot them using Matplotlib in 3D.

The vast majority of this code is taken from here. All I have done is looped through the bands, extracted the reflectance values and plotted the result.

Firstly, I made a function (from the above link) to extract the values from the satellite image.

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2017/01/code1.png)

I called this function 'training points' and I passed ‘raster’ (the file name of 1 band) and ‘shp’ (the shapefile containing my 8 points). I then created 3 empty lists: lsx, lsy and lsz where I am going to append the x and y coordinates from the shapefile and the z (the value of the reflectance in the raster). Again this function is adapted from code I found in the above link.

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2017/01/code2.png)

Secondly I built the 3d plot and looped through the directory containing the raster images. Once I have found an image I call the training points function and with the resulting data plot it. I have built a list with colours that I assign for each layer as it is created. After all the rasters have been found I plot the graph.

![alt tag](http://www.acgeospatial.co.uk/wp-content/uploads/2017/01/extract_points.gif)

It took 0.09 seconds to run on my computer, which is more than good enough. The point in the ‘brown’ field has a different spectral profile to the others. I hope this gives an idea of the different spectral properties of different land cover types.

Do you want to find out about more of my work? Http://www.acgeospatial.co.uk

