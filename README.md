# GlitchArtGenerator
Pixel sorting glitch art generator I made in Python

## Use:
To use, put this script in a directory where you have image files you wish to turn into glitch art.

Edit the "fileName" variable in "glitchArt.py" to be the file name of the image (you must include the file extension). Next, change the "outputFileName" variable to the name you wish to call the new glitch version of the image (you must include the file extension). 

Finally, run the script. The new image will open in your default image program. This process will not ruin the original image, but it will save a new image with the changes.

The script will pick a random location to sort the pixels in a vertical stripe and a horizontal stripe. You can run the script multiple times on a a single image and get different results every time.

NOTE: You need the PIL (Pillow) module to be able to run this code
