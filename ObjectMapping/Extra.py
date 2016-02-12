import cv2
from imutils.object_detection import non_max_suppression
from imutils import paths

import numpy as np

import imutils

import os
from matplotlib import pyplot as plt


def binarizeImage(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    plt.imshow(thresh)
    plt.show()


def surfDescriptorsMatching(self,refImage,threshold=2):

        surf = cv2.SURF(1)

        #Find descriptors for self.image
        kp1, des1 = surf.detectAndCompute(self.image, None)
        kp2, des2 = surf.detectAndCompute(refImage, None)

        # Create and initiate matcher object
        matcher = cv2.BFMatcher()
        matches = matcher.knnMatch(des1, des2, k=2)

        # Apply test
        good = []
        for m,n in matches:
            if m.distance < 0.50*n.distance:
                good.append([m])

        # Draw matches
        print len(good)

        if len(good) >= threshold:
            return True
        else:
            return False

def pedestrainDetection(self,image):

    # Set local image variable
    image = self.image

    # initialize the HOG (Histogram of Oriented descriptor)
    hog = cv2.HOGDescriptor()
    # Get SVM to be pre-trained person detector
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Resize the image to reduce detection time and increase accuracy
    image = imutils.resize(self.image, width=min(400, self.image.shape[1]))
    orig = image.copy()

    # Detect people in image
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
    padding=(8, 8), scale=1.05)

    # draw the original bounding boxes
    for (x, y, w, h) in rects:
        cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Apply non-maxima suppression to the bounding boxes using a
    # fairly large overlap threshold to try to maintain overlapping
    # boxes that are still people
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    # Draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

    # Show some information on the number of bounding boxes
    plt.imshow(image)
    plt.show()


