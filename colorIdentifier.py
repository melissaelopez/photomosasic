import struct
from PIL import Image
import scipy
import scipy.misc
import scipy.cluster
import numpy
from scipy.cluster.vq import vq, kmeans, whiten


NUM_CLUSTERS = 5

print ("the program is running...")

image = Image.open('test.jpg')
image = image.resize((150,150))
imageArray = numpy.asarray(image)
shape = imageArray.shape
imageArray = imageArray.reshape(numpy.prod(shape[:2]),shape[2])

print ("finding clusters")
codes, dist = scipy.cluster.vq.kmeans(imageArray.astype(float), NUM_CLUSTERS)
print ("cluster centers: \n", codes)

vecs, dist = scipy.cluster.vq.vq(imageArray, codes)
counts, bins = scipy.histogram(vecs, len(codes))

index_max = scipy.argmax(counts)
peak = codes[index_max]
# color = ''.join(int(binascii.hexlify(c)) for c in peak)
color = ''.join( '{0:02x}'.format(int(c)) for c in peak)
print ("dominant color is %s (#%s)" %(peak, color))
# print ('{0:02x}'.format(int(peak[0])))