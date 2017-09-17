import cv2
import numpy as np


image = cv2.imread('formula.jpg')

B, G, R = cv2.split(image)

zeros = np.zeros((image.shape[0], image.shape[1]), np.uint8)
cv2.imshow('Original', image)
cv2.imshow('Blue Channel', cv2.merge([B, zeros, zeros]))
cv2.imshow('Green Channel', cv2.merge([zeros, G, zeros]))
cv2.imshow('Red Channel', cv2.merge([zeros, zeros, R]))
cv2.waitKey(0)
cv2.destroyAllWindows