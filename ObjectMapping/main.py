from matplotlib import pyplot as plt

import os
import numpy as np
import ObjectMapping


def main():
    path = os.getcwd()+"\..\Data\image05.jpg"
    image = plt.imread(path)

    #plt.imshow(image)
    #plt.show()

    objectMapping = ObjectMapping.ObjectMapping(image)
    objectMapping.binarizeImage()
    #objectMapping.mapObjects()


if __name__ == '__main__':
	main()
