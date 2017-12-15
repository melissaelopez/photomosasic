# PHOTOMOSAIC
Final Project for NYU Large Scale Web Applications taught by Professor Yair Sovran  
Group Members: JD Choi, Zachary Lin, Melissa Lopez, and William Chen

## Project Objective
To build a Django application with an image classifier that allows the user to:
1. Have their images classified by dominant color and stored in our file system  
![alt text](https://preview.ibb.co/fUxNQR/Screen_Shot_2017_12_15_at_2_40_36_PM.png)
2. Upload a source image and generate photomosaic from it (using images already in our system)  
![alt text](https://preview.ibb.co/iJKQem/Screen_Shot_2017_12_15_at_2_40_43_PM.png)

## Core Technologies Used
* Google Cloud Platform --> (deployment)
* Google Cloud Storage --> (image storage)
* Python Imaging Library (PIL) --> (image classification + mosaic construction)
* NumPy Library --> (image classification)

## Code Organization
`/mysite` --> boilerplate Django app files  
`/myvenv` --> virtual environment files  
`/photomosaic` --> application (including image classification by color + mosaic code)  

## Image Classification + Mosaic Construction Files
* `color_id.py`  
  * Returns a color classification tuple of the form: ( 'color_name' , (R, G, B) )
* `get_mosaic.py`  
  * Returns "mosaic map" representing the colors of tiles needed for the final photomoasic
* `get_tile_requirements.py`  
  * Normalizes size and aspect ratio of source image + tile images
* `collage.py`  
  * Constructs final moasic based on mosaic map
