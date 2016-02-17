
import cv2

class ObjectClassification:

    LABEL_HUMANS = "human"
    LABEL_ANIMALS = "animal"
    LABEL_THINGS = "thing"

    # Labels on each object to see which category they belong to
    objects = []
    # Number of images in each object
    n = 0
    # Starting 'x' positions of rectangles around mapped objects
    start_x = []
    # Starting 'y' positions of rectangles around mapped objects
    start_y = []
    # Widths of rectangles around mapped objects
    widths = []
    # Heights of rectangles around mapped objects
    heights = []

    def __init__(self, image, start_x, start_y, widths, heights):
        self.image = image
        self.start_x = start_x
        self.start_y = start_y
        self.widths = widths
        self.heights = heights

    def ClassifyAllObjects(self):
        objects = [self.classifyObject(self.startingPosY[i], self.startingPosY[i], self.widths[i],
                                  self.heights[i]) for i in range(0,self.n)]

    def classifyObject(self, PosX, PosY, width, height):

        pass

    '''
    Loops through all sub-images and detects if any sub-image matches
    with the reference image provided by the user.
    '''

    def findImage(self, image_ref,threshold=2):

        # Note: self.image() first takes height and then width

        sub_images = []
        for i in range(0,len(self.widths)):
            sub_images.append(self.image[self.start_y[i]:(self.start_y[i]+self.heights[i]),
                              self.start_x[i]:(self.start_x[i]+self.widths[i])])

        return [self.matchSURFDescriptors(sub_image, image_ref) for sub_image in sub_images]

    '''
    Matches SURF Descriptors of two images and returns a boolean
    indicating if length of good matches exceeds threshold.
    '''

    def matchSURFDescriptors(self, image, image_ref, threshold = 4):

        # TRADE-OFF: Threshold can be adjusted to see where we get optimum value.
        surf = cv2.SURF(400)

        #Find descriptors for self.image
        kp1, des1 = surf.detectAndCompute(image, None)
        kp2, des2 = surf.detectAndCompute(image_ref, None)

        # Create and initiate matcher object
        matcher = cv2.BFMatcher()
        matches = matcher.knnMatch(des1, des2, k=2)

        # Apply test
        good = []
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                good.append([m])

        # Draw matches
        #print "Good Matches: ", len(good)

        if len(good) >= threshold:
            return True
        else:
            return False

    def getObjects(self):
        return self.objects
