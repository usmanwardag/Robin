
import os
from os import path
import sys
import ObjectClassification as classification
from matplotlib import pyplot
import ObjectMapping

sys.path.insert(0, path.abspath('..'))

def main():
    path_original = os.getcwd()+"\..\Data\imageMatching01.jpg"
    path_ref = os.getcwd()+"\..\Data\imageMatching02.jpg"

    image_original = plt.imread(path_original,0)
    image_ref = plt.imread(path_ref,0)

    object_mapping = ObjectMapping(originalImage)
    object_mapping.mapObjects()
    startingPosX, startingPosY, widths, heights = object_mapping.getObjects()

    #classificationObject = classification.ObjectClassification(originalImage, startingPosX,
    #                                            startingPosY, widths, heights)

    #classificationObject.matchImage(refImage)


if __name__ == '__main__':
    main()
