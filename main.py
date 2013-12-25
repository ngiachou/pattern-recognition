import numpy as np
import scipy
import pylab
import pymorph
import mahotas
from scipy import ndimage

drs = mahotas.imread('droso.JPG')

pylab.imshow(drs)
pylab.show()

#print drs.shape
#print drs.dtype
#print drs.max()
#print drs.min()
drsf = ndimage.gaussian_filter(drs,3)
T = mahotas.thresholding.otsu(drsf)
pylab.imshow(drsf > T)
pylab.show()

labeled,nr_objects = ndimage.label(drsf > T)
print nr_objects
pylab.imshow(labeled)
pylab.jet()
pylab.show()
