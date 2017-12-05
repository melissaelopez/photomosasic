from PIL import Image
from get_tile_requirements import resize_and_crop
from get_tile_requirements import get_tile_classification
from collage import collage

# filename = '8.jpg'
# desired_source_dimmensions = (1000,1000)
# tiles_across = 10
# tiles_down = 10
# tile_dimmensions = (100, 100)


def make_mosaic(filename, desired_source_dimmensions, tiles_across, tiles_down, tile_dimmensions):
    mosaic_map = []
    for i in range(tiles_across * tiles_down):
        source_image = resize_and_crop(filename, desired_source_dimmensions)
        mosaic_map.append(get_tile_classification(source_image, i, tiles_across, tiles_down, tile_dimmensions))
    print("mapping is done")
    new_im = collage(mosaic_map, tile_dimmensions, tiles_across, tiles_down, tile_dimmensions[0])
    print("displaying mosaic")
    return new_im

# make_mosaic(filename, desired_source_dimmensions, tiles_across, tiles_down, tile_dimmensions)
