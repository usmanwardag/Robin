
import os
from os import path
import sys
from matplotlib import pyplot as plt

sys.path.append(path.abspath('../ObjectMapping'))


def main():
    from ObjectMapping.ObjectMapping import ObjectMapping
    originalImagePath = os.getcwd()+"\..\Data\personInRoom07.jpg"
    originalImage = plt.imread(originalImagePath)

    objectMapping = ObjectMapping(originalImage)
    objectMapping.mapObjects()

if __name__ == '__main__':
    main()
