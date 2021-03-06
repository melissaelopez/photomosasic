from PIL import Image
import os, random
from get_tile_requirements import resize_and_crop

from google.cloud import storage
import StringIO

# Collage together images
images_to_mosaic_together = ["1.jpg","2.jpg","3.jpg",
                            "4.jpg","5.jpg","6.jpg",
                            "7.jpg","8.jpg","9.jpg"]

# def create_tiles(mosaic_map, tile_dimmensions):
#     tiles = []
#     for item in mosaic_map:
#         new_tile = Image.new('RGB', tile_dimmensions, (int(item[1][0]), int(item[1][1]), int(item[1][2])))
#         tiles.append(new_tile)
#     return tiles
#
# def collage(images, mosaic_width, mosaic_height, tile_size):
#     # Resize images for tiles
#     tiles = []
#     for image in images:
#         my_image = image.resize((tile_size, tile_size))
#         tiles.append(my_image)
#
#     #creates a new empty image, RGB mode, and size 300 by 300 (for this example)
#     new_im = Image.new('RGB', (tile_size * mosaic_height,tile_size * mosaic_height))
#
#     #Iterate through a 3 by 3 grid with 100px spacing, to place my image
#     count = 0;
#     for i in range(0, tile_size * mosaic_height, tile_size):
#         for j in range(0, tile_size * mosaic_height, tile_size):
#             new_im.paste(images[count], (i,j))
#             count += 1
#     new_im.show()

def collage(mosaic_map, tile_dimmensions, mosaic_width, mosaic_height, tile_size):
    # item = mosaic_map[0]
    # new_tile = Image.new('RGB', tile_dimmensions, (int(item[1][0]), int(item[1][1]), int(item[1][2])))
    # new_tile.show()
    images = []
    print("creating tiles ...")
    # UNCOMMENT THIS SECTION TO GENERATE SINGLE COLORED TILES FROM SCRATCH
    for item in mosaic_map:
        #new_tile = Image.new('RGB', tile_dimmensions, (int(item[1][0]), int(item[1][1]), int(item[1][2])))


        storage_client = storage.Client()
        bucket = storage_client.get_bucket('photomosaic_storage')
        
        #retrieving items from file system based on color
        color = item[0]
        path =  'media/photos/' + color
        image_list = bucket.list_blobs(prefix=path)

        
        image = 0
        #iterate through images while skipping through directory name
        #get the newest image
        dir = 1
        for blob in image_list:
            if (dir == 1):
                dir = 0
            else:
                image = blob

        #Download the image as a string and convert to stringIO
        image_from_bucket = StringIO.StringIO()
        image_from_bucket.write(image.download_as_string())
        image_from_bucket.seek(0)

        #resize image
        bg = resize_and_crop(image_from_bucket, tile_dimmensions).convert("RGBA")
        fg = Image.new('RGBA', tile_dimmensions, (int(item[1][0]), int(item[1][1]), int(item[1][2])))
        new_tile = Image.blend(bg, fg, .9)
        
        #add image to list for mosaic formation
        images.append(new_tile)
                
        image_from_bucket.close()


            #Code for retrieving from a local file system
##        #retrieving items from file system based on color
##        color = item[0]
##        path = os.path.join('.', 'media', 'photos', color)
##        
##        #pick a random image from folder
##        #make sure all folders exist and have at least one image beforehand
##        image_list = os.listdir(path)
##        image_index = random.randrange(0, len(image_list))
##
##        #get the path of chosen image
##        image_name = image_list[image_index]
##        image_path = os.path.join(path, image_name)
##
##       #resize image and append to array
##        if os.path.isfile(image_path):
##            bg = resize_and_crop(image_path, tile_dimmensions).convert("RGBA"))
##            fg = Image.new('RGBA', tile_dimmensions, (int(item[1][0]), int(item[1][1]), int(item[1][2])))
##            new_tile = Image.blend(bg, fg, .9)
##            images.append(new_tile)

    print("resizing tiles ...")
    # Resize images for tiles
    tiles = []
    for image in images:
        my_image = image.resize((tile_size, tile_size))
        tiles.append(my_image)

    print("create collage base  ...")
    #creates a new empty image, RGB mode, and size 300 by 300 (for this example)
    new_im = Image.new('RGB', (tile_size * mosaic_width,tile_size * mosaic_height))

    print("stiching collage  ...")
    #Iterate through a 3 by 3 grid with 100px spacing, to place my image
    count = 0;
    for i in range(0, tile_size * mosaic_height, tile_size):
        for j in range(0, tile_size * mosaic_height, tile_size):
            # (i, j) vs (j, i) --> double check that this is exactly what you want
            new_im.paste(images[count], (j,i))
            count += 1
            if (count >= len(images)):
                break
    new_im.show()
    return new_im
