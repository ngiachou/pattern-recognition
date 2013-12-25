import numpy as np
import scipy
import pylab
import pymorph
import mahotas
from scipy import ndimage

drs = mahotas.imread('droso.JPG')

drsf = ndimage.gaussian_filter(drs, 3)
rmax = pymorph.regmax(drsf)
pylab.imshow(pymorph.overlay(drs, rmax))
pylab.show()
