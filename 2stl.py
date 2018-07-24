from pylab import imread
from stl_tools import numpy2stl
from scipy.misc import imresize
from scipy.ndimage import gaussian_filter

A = 256 * imread("cantcatchme-2-fs.png")
A = imresize(A, (512, 512))
A = A[:, :, 2] + 1.0*A[:,:, 0] # Compose RGBA channels to give depth
A = gaussian_filter(A, 1)  # smoothing
numpy2stl(A, "gary.stl", scale=0.1, mask_val=5., solid=True)
