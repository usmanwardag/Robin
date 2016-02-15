
import os
from os import path
import sys
from matplotlib import pyplot as plt

sys.path.insert(0, path.abspath('..'))
#sys.path.append(path.abspath('../ObjectMapping'))
print path.abspath('../ObjectMapping')


def main():
    from ObjectMapping.ObjectMapping import ObjectMapping
    originalImagePath = os.getcwd()+"\..\Data\personInRoom01.jpg"
    originalImage = plt.imread(originalImagePath)
    objectMapping = ObjectMapping(originalImage)
    objectMapping.mapObjects()
    startingPosX, startingPosY, widths, heights = objectMapping.getObjects()

if __name__ == '__main__':
    main()
