import cv2
import numpy as np

def flip(image):
    temp = [] 
    for row in image:
        row = row[::-1]
        temp.append(row)
    return np.array(temp)

if __name__ == "__main__":
    image = cv2.imread('puppy.jpeg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    flipped = flip(image)
    cv2.imshow("flipped image", flipped)
    cv2.waitKey(0)