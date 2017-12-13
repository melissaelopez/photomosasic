from PIL import Image
import os, random

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

        #retrieving items from file system based on color
        color = item[0]
        path = os.path.join('.', 'media', 'photos', color)
        
        #pick a random image from folder
        #make sure all folders exist and have at least one image beforehand
        image_list = os.listdir(path)
        image_index = random.randrange(0, len(image_list))

        #get the path of chosen image
        image_name = image_list[image_index]
        image_path = os.path.join(path, image_name)

        #open the image and add it to the images list
        if os.path.isfile(image_path):
            images.append(Image.open(image_path))
                

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
