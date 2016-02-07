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
        objects = [classifyObject(self.startingPosY[x], self.startingPosY[i], self.widths[i],
                                  self.heights[i]) for i in range(1,n)]

    def classifyObject(self, PosX, PosY, width, height):

        if objectIsHuman():
            return self.LABEL_HUMANS

        if objectIsAnimal():
            return self.LABEL_ANIMALS

        if objectIsThing():
            return self.LABEL_THINGS

    def objectIsHuman(self):

        # TO DO:  RUN MACHINE LEARNING ALGORITHM AGAINST HUMANS
        return boolean

    def objectIsAnimal(self):

        # TO DO:  RUN MACHINE LEARNING ALGORITHM AGAINST ANIMALS
        return boolean

    def objectIsThing(self):

        # TO DO:  RUN MACHINE LEARNING ALGORITHM AGAINST THINGS
        return boolean

    def getObjects(self):
        return self.objects
