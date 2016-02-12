
import cv2
import math
from matplotlib import pyplot as plt
import numpy as np
import os

from sklearn import cluster
from sklearn.cluster import KMeans


class ObjectMapping:

    n = 0
    # Starting 'x' positions of rectangles around mapped objects
    startingPosX = []
    # Starting 'y' positions of rectangles around mapped objects
    startingPosY = []
    # Widths of rectangles around mapped objects
    widths = []
    # Heights of rectangles around mapped objects
    heights = []

    def __init__(self, image):
        self.image = image

        # Resize image maintaining the aspect ratio
        r = 400.0 / image.shape[1]
        self.image = self.resizeImage(self.image,400,int(self.image.shape[0] * r))


    def resizeImage(self, image, xPixels, yPixels):
        return cv2.resize(image,(xPixels,yPixels))

    def mapObjects(self):

        points = self.getSurfPoints()
        self.startingPosX, self.startingPosY, self.widths,self.heights = self.clusterSurfPoints(points)
        self.n = len(self.startingPosX)

        self.getObjects()

    def getSurfPoints(self):
        # Initialize the HOG (Histogram of Oriented descriptor)
        surf = cv2.SURF(300)
        kp, des = surf.detectAndCompute(self.image, None)

        # Get x,y coordinates of all surf points
        points = [point.pt for point in kp]
        points = np.array(points)
        return points

    def clusterSurfPoints(self, points, threshold = 200):

        # Set local image variable
        image = self.image

        # Show figure
        fig = plt.figure()
        plt.imshow(image)

        # Start with 0 inertia and 10 clusters
        inertia = 0
        n_clusters = 10

        # The code below determines the ideal number of clusters by evaluating the
        # value of inertia. Experimentally, inertia of 200 was found to be the best
        # fit while determining number of clusters.

        while inertia<=200:

            # Find clusters and fit on data
            k_means = cluster.KMeans(n_clusters=n_clusters)
            k_means.fit(points)

            # Find cluster centers
            cluster_centers = np.array(k_means.cluster_centers_)

            # Inertia is the sum of distannces between all clusters
            inertia = math.sqrt(k_means.inertia_/n_clusters)

            if n_clusters == 2:
                break

            if inertia < 200:
                n_clusters = n_clusters - 1


        print "Total Clusters: ", n_clusters
        print "Final Inertia: ", inertia

        # Draw Rectangles
        w = h = [100 for center in cluster_centers]
        left_x = [int(center[0] - w[0]/2) for center in cluster_centers]
        left_y = [int(center[1] - h[0]/2) for center in cluster_centers]

        for i in range(1,len(left_x)):
            cv2.rectangle(image, (left_x[i],left_y[i]),(left_x[i]+w[0],left_y[i]+w[0]),(0, 255, 0), 2)

        plt.show()

        return left_x, left_y, w, h

    def getNumberOfObjects(self):
        return self.n

    def getObjects(self):
        return self.startingPosX, self.startingPosY, self.widths, self.heights

