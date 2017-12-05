from PIL import Image
from color_id import get_classification

# this function is for cropping and resizing (normalizes source image to (1000px x 1000px))

def resize_and_crop(filename, size):
    # If height is higher we resize vertically, if not we resize horizontally
    img = Image.open(filename)
    # Get current and desired ratio for the images
    img_ratio = img.size[0] / float(img.size[1])
    ratio = size[0] / float(size[1])
    #The image is scaled/cropped vertically or horizontally depending on the ratio
    if ratio > img_ratio:
        img = img.resize((size[0], size[0] * img.size[1] / img.size[0]),
                Image.ANTIALIAS)
        box = (0, 0, img.size[0], size[1])
        img = img.crop(box)
    elif ratio < img_ratio:
        img = img.resize((size[1] * img.size[0] / img.size[1], size[1]),
                Image.ANTIALIAS)
        box = (0, 0, size[0], img.size[1])
        img = img.crop(box)
    else :
        img = img.resize((size[0], size[1]),
                Image.ANTIALIAS)
    return img

def get_tile_classification(img, tile_number, tiles_across, tiles_down, tile_size):
    tile_x = (tile_number % tiles_across) * tile_size[0]
    tile_y = (tile_number / tiles_down) * tile_size[1]

    box = (tile_x, tile_y, tile_x + tile_size[0], tile_y + tile_size[1])
    img = img.crop(box)
    return get_classification('', img)


# resize_and_crop('8.jpg', size)
# source_image = resize_and_crop('8.jpg', (1000,1000))
# source_image.save('8-resized.jpg')
