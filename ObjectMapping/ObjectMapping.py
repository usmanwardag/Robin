
import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

class ObjectMapping:

    n = 0
    # Starting 'x' positions of rectangles around mapped objects
    startingPosX = []
    # Starting 'y' positions of rectangles around mapped objects
    startingPosY = []
    # Widths of rectangles around mapped objects
    widths = []
    # Heights of rectangles around mapped objects
    heights = []

    def __init__(self, image):
        self.image = image

    def resizeImage(self, image, xPixels, yPixels):
        # TO DO: Resize image
        pass

    def mapObjects(self):

        # Resize the image to 400*400 pixels

        self.resizeImage(self.image, 400, 400)

        # TO DO: Implement algorithm to calculate objects

        # TO DO: Set n
        # TO DO: Populate lists
        pass

    def binarizeImage(self):
        gray = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        plt.imshow(thresh)
        plt.show()

    def getNumberOfObjects(self):
        return self.n

    def getObjects(self):
        return self.startingPosX, self.startingPosY, self.widths, self.heights
