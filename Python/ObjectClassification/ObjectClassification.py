import cv2

from matplotlib import pyplot as plt
import numpy as np

class ObjectClassification:

    LABEL_HUMANS = "human"
    LABEL_ANIMALS = "animal"
    LABEL_THINGS = "thing"

    # Labels on each object to see which category they belong to
    objects = []
    # Number of images in each object
    n = 0
    # Starting 'x' positions of rectangles around mapped objects
    startingPosX = []
    # Starting 'y' positions of rectangles around mapped objects
    startingPosY = []
    # Widths of rectangles around mapped objects
    widths = []
    # Heights of rectangles around mapped objects
    heights = []

    def __init__(self, image, startingPosX, startingPosY, widths, heights):
        self.image = image
        self.startingPosX = startingPosX
        self.startingPosY = startingPosY
        self.widths = widths
        self.heights = heights
        # Resize image maintaining the aspect ratio
        r = 400.0 / image.shape[1]
        self.image = self.resizeImage(self.image,400,int(self.image.shape[0] * r))


    def resizeImage(self, image, xPixels, yPixels):
        return cv2.resize(image,(xPixels,yPixels))

    def ClassifyAllObjects(self):
        objects = [self.classifyObject(self.startingPosY[i], self.startingPosY[i], self.widths[i],
                                  self.heights[i]) for i in range(1,self.n)]

    def classifyObject(self, PosX, PosY, width, height):

        if self.objectIsHuman():
            return self.LABEL_HUMANS

        if self.objectIsAnimal():
            return self.LABEL_ANIMALS

        if self.objectIsThing():
            return self.LABEL_THINGS

    def matchImage(self, refImage,threshold=2):

        subImages = [self.image[self.startingPosX[i]:(self.startingPosX[i]+self.widths[i]),
        self.startingPosY[i]:(self.startingPosY[i]+self.heights[i])] for i in range(1,len(self.widths))]

        #matchResults = [self.matchSURFDescriptors(subImage,refImage) for subImage in subImages]
        #print matchResults

        refImage = self.resizeImage(refImage,self.widths[0]/12,(self.widths[0]/12)*(subImages[0].shape[0]/subImages[0].shape[1]))

        for subImage in subImages:
            self.templateMatching(subImage,refImage)

    def matchSURFDescriptors(self, image, refImage, threshold = 2):

        surf = cv2.SURF(400)

        plt.imshow(image)
        plt.show()

        #Find descriptors for self.image
        kp1, des1 = surf.detectAndCompute(self.image, None)
        kp2, des2 = surf.detectAndCompute(refImage, None)

        # Create and initiate matcher object
        matcher = cv2.BFMatcher()
        matches = matcher.knnMatch(des1, des2, k=2)

        print "Matches: ", matches

        # Apply test
        good = []
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                good.append([m])

        # Draw matches
        print "Good Matches: ", len(good)

        if len(good) >= threshold:
            return True
        else:
            return False


    def templateMatching(self,image,template):

        img2 = image.copy()
        w, h, c = template.shape
        # All the 6 methods for comparison in a list
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED',
                   'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

        for meth in methods:
            img = img2.copy()
            method = eval(meth)
            # Apply template Matching
            res = cv2.matchTemplate(img,template,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            print "Locations: ",min_loc,max_loc

            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc

            w = -20
            h = +20

            print "Values: ", min_val, max_val

            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(img,top_left, bottom_right, 255, 2)
            plt.subplot(111),plt.imshow(img,cmap = 'gray')
            plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            plt.suptitle(meth)
            plt.show()

    def objectIsHuman(self):

        # TO DO:  RUN MACHINE LEARNING ALGORITHM AGAINST HUMANS
        return True

    def objectIsAnimal(self):

        # TO DO:  RUN MACHINE LEARNING ALGORITHM AGAINST ANIMALS
        return True

    def objectIsThing(self):

        # TO DO:  RUN MACHINE LEARNING ALGORITHM AGAINST THINGS
        return True

    def getObjects(self):
        return self.objects
