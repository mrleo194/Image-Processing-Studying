import cv2

def flop(image):
    image = image[::-1]
    return image

if __name__ == "__main__":
    image = cv2.imread('puppy.jpeg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    flipped = flop(image)
    cv2.imshow("flopped image", flipped)
    cv2.waitKey(0)
