import cv2
import numpy as np

def flip(image):
    temp = [] 
    for row in image:
        row = row[::-1]
        temp.append(row)
    return np.array(temp)

def flip_horizontal(image):
    temp = np.asarray(image)
    h = image.shape[0]
    w = image.shape[1]
    for i in range(h):
        for j in range(w//2):
            temp = image[i][j]
            image[i][j] = image[i][w - 1 - j]
            image[i][w - 1 - j] = temp
    return image

if __name__ == "__main__":
    image = cv2.imread('puppy.jpeg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
    flipped = flip_horizontal(image)
    cv2.imshow("flipped image", flipped)
    cv2.waitKey(0)
    #print(flipped)