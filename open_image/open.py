import cv2
from argparse import ArgumentParser

# agrpase
parse = ArgumentParser()
parse.add_argument("-i", "--image", required=True, help="path to image")
args = vars(parse.parse_args())

# read 8-bit gray scale
image1 = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)
print("flags: cv2.IMREAD_GRAYSCALE")
print("Image size: {}, type: {}".format(image1.shape, image1.dtype))
print("===============================================")
# read 8-bit color image
image2 = cv2.imread(args["image"], cv2.IMREAD_COLOR)
print("flags: cv2.IMREAD_COLOR")
print("Image size: {}, type: {}".format(image2.shape, image2.dtype))
print("===============================================")
# read transparent PNG, TIFF image
image3 = cv2.imread(args["image"], cv2.IMREAD_UNCHANGED)
print("flags: cv2.IMREAD_UNCHANGED")
print("Image size: {}, type: {}".format(image3.shape, image3.dtype))
print("===============================================")

