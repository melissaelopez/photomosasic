import struct
from PIL import Image
import scipy
import scipy.misc
import scipy.cluster
import numpy
from scipy.cluster.vq import vq, kmeans, whiten

NUM_CLUSTERS = 5

print ("the program is running...")

color_classifiation = ['']
tuning = 20

# this function gets the dominant color in hex and rgb of a given photo
# returns [r, g, b] as a list
def getDominantColorHex(filename, img=None):
    if (img == None):
        image = Image.open(filename)
    else:
        image = img
    image = image.resize((tuning,tuning))
    imageArray = numpy.asarray(image)
    shape = imageArray.shape
    imageArray = imageArray.reshape(numpy.prod(shape[:2]),shape[2])

    # print ("finding clusters")
    codes, dist = scipy.cluster.vq.kmeans(imageArray.astype(float), NUM_CLUSTERS)
    # print ("cluster centers: \n", codes)

    vecs, dist = scipy.cluster.vq.vq(imageArray, codes)
    counts, bins = scipy.histogram(vecs, len(codes))

    index_max = scipy.argmax(counts)
    peak = codes[index_max]
    # color = ''.join(int(binascii.hexlify(c)) for c in peak)
    color = ''.join( '{0:02x}'.format(int(c)) for c in peak)
    # UNCOMMENT ME TO SEE RESULT COLOR
    # print ("dominant color is %s (#%s)" %(peak, color))
    # print ('{0:02x}'.format(int(peak[0])))
    return peak

# this function converts the RGB value into an HSL value
# assumes r, g, b are in domain [0, 255]
# h: range [0, 360]
# s: range [0, 100]
# l: range [0, 100]
# returns [h, s, l] as a list
def rgbToHsl(peak):

    r = peak[0] / 255
    g = peak[1] / 255
    b = peak[2] / 255
    maxVal = max(r, g, b)
    minVal = min(r, g, b)
    h = (maxVal + minVal) / 2
    s = (maxVal + minVal) / 2
    l = (maxVal + minVal) / 2

    if (maxVal == minVal):
        h = s = 0
    else :
        d = maxVal - minVal
        s = d / (2 - maxVal - minVal) if l > 0.5 else d / (maxVal + minVal)
        if maxVal == r:
            h = (g - b) / d + (6 if g < 6 else 0)
        elif (maxVal == g):
            h = (b - r) / d + 2
        elif (maxVal == b):
            h = (r - g) / d + 4
        h /= 6
    # print("The color in HSL is:" + str([h * 360, s * 100, l * 100]))
    return [h * 360, s * 100, l * 100]

# this function takes a file(by name or by Image object), and classifies it by color
def get_classification(filename, img=None):
    if (img == None):
        rgb = getDominantColorHex(filename)
    else:
        rgb = getDominantColorHex(filename, img)
    hsl = rgbToHsl(rgb)
    if (hsl[2] < 10):
        return ('black', rgb)
    elif (hsl[2] > 90):
        return ('white', rgb)
    elif (hsl[0] < 40):
        return ('orange', rgb)
    elif (hsl[0] < 65):
        return ('yellow', rgb)
    elif (hsl[0] < 160):
        return ('green', rgb)
    elif (hsl[0] < 180):
        return ('cyan', rgb)
    elif (hsl[0] < 255):
        return ('blue', rgb)
    elif (hsl[0] < 290):
        return ('purple', rgb)
    elif (hsl[0] < 330):
        return ('pink', rgb)
    else:
        return ('red', rgb)
