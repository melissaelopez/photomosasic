# PHOTOMOSAIC
Final Project for NYU Large Scale Web Applications taught by Professor Yair Sovran

Group Members: JD Choi, Zachary Lin, Melissa Lopez, and William Chen

## Project Objective
To build a Django application with an image classifier that allows the user to:
1. Have their images classified by dominant color and stored in our file system

![alt text](https://preview.ibb.co/fUxNQR/Screen_Shot_2017_12_15_at_2_40_36_PM.png)
2. Upload a source image and generate photomosaic from it (using images already in our system)

![alt text](https://preview.ibb.co/iJKQem/Screen_Shot_2017_12_15_at_2_40_43_PM.png)

## Code Organization
`mysite` --> boilerplate Django app files

`myvenv` --> virtual environment files

`photomosaic` --> application (including color classification + mosaic implementation code)


## Color Classification + Mosaic Implementation Files
* collage.py
* color_id.py
* get_mosaic.py
* get_tile_requirements.py
