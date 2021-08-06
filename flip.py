import cv2
import numpy as np

def flip(image):
    #new_image = np.asarray(image)
    rows = image.shape[0]
    cols = image.shape[1]
    temp = []
    new_col = []

    
    for row in image:
        #for i in range(rows)
        #first = layer
        #last = rows-layer-1
        #for i in range(first, last):  
        #new_image[i, cols-1-j] = image[i, j]
            #new_col = image[layer, i]
        # image[:, col] = temp[:, cols-1-col]
        # temp[:, cols-1-col] = new_image[:, col]
        # temp.append(col)
#image = image[::-1]
        #new_col = new_col
        row = row[::-1]
        temp.append(row)

    return np.array(temp)

def flop(image):
    image = image[::-1]
    return image

if __name__ == "__main__":
    image = cv2.imread('puppy.jpeg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    flipped = flop(image)
    cv2.imshow("flipped image", flipped)
    cv2.waitKey(0)
    #print(flipped.shape)
    #print(image.shape[0])

