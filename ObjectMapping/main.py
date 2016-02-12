from matplotlib import pyplot as plt

import cv2
import os
import numpy as np
import ObjectMapping


def main():


    images = ['01','02','03','04','05','06','07','09','10',
              '11','12','13','14','15']
    paths = [os.getcwd()+"\..\Data\person"+images[i]+".jpg"
             for i in range(1,len(images))]
    #referenceImages = [plt.imread(path) for path in paths]

    originalImagePath = os.getcwd()+"\..\Data\personInRoom07.jpg"
    originalImage = plt.imread(originalImagePath)

    objectMapping = ObjectMapping.ObjectMapping(originalImage)
    objectMapping.mapObjects()

if __name__ == '__main__':
	main()
