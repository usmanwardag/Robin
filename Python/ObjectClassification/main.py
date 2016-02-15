
import os
from os import path
import sys
import ObjectClassification as classification
from matplotlib import pyplot as plt

sys.path.insert(0, path.abspath('..'))

def main():
    from ObjectMapping.ObjectMapping import ObjectMapping
    originalImagePath = os.getcwd()+"\..\Data\imageMatching03.jpg"
    refImagePath = os.getcwd()+"\..\Data\imageMatching02.jpg"
    originalImage = plt.imread(originalImagePath,0)
    refImage = plt.imread(refImagePath,0)

    mappingObject = ObjectMapping(originalImage)
    mappingObject.mapObjects()
    startingPosX, startingPosY, widths, heights = mappingObject.getObjects()

    classificationObject = classification.ObjectClassification(originalImage, startingPosX,
                                                startingPosY, widths, heights)

    classificationObject.matchImage(refImage)


if __name__ == '__main__':
    main()
