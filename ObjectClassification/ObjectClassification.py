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

    def resizeImage(self, image, xPixels, yPixels):
        # TO DO: Resize image
        pass

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
