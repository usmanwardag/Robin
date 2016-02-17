
import cv2
import math
from matplotlib import pyplot as plt
import numpy as np

from sklearn import cluster

class ObjectMapping:

    n = 0
    # Starting 'x' positions of rectangles around mapped objects
    startingPosX = []
    # Starting 'y' positions of rectangles around mapped objects
    startingPosY = []
    # distance from center of each object
    distanceFromCenter = []
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
        self.startingPosX, self.startingPosY, self.widths ,self.heights = self.clusterSurfPoints(points)
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

            # Inertia is the sum of distances between all clusters
            inertia = math.sqrt(k_means.inertia_/n_clusters)

            if n_clusters == 2:
                break

            if inertia < 200:
                n_clusters = n_clusters - 1

        print "Total Clusters: ", n_clusters
        print "Final Inertia: ", inertia

        # Initialize widths and heights
        widths = []
        heights = []

        w = 100 * self.image.shape[1]/400
        h = 100 * self.image.shape[0]/400

        print "Scaled width and height: ",w,h
        print "Cluster Centers", cluster_centers

        for i in range(0,n_clusters):
            if (cluster_centers[i][0]+w/2) > self.image.shape[1]:
                print (cluster_centers[i][0]+w/2)
                widths.append(int(self.image.shape[1]-cluster_centers[i][0])*2)
                print "Width - Case 1"
            elif (cluster_centers[i][0]-w/2) < 0:
                widths.append(int(cluster_centers[i][0]*2))
                print "Width - Case 2"
            else:
                widths.append(w)
                print "Width - Case Default"

            if (cluster_centers[i][1]+h/2) > self.image.shape[0]:
                heights.append(int(self.image.shape[0]-cluster_centers[i][1])*2)
                print "Height - Case 1"
            elif (cluster_centers[i][1]-h/2) < 0:
                heights.append(int(cluster_centers[i][1]*2))
                print "Height - Case 2"
            else:
                heights.append(h)
                print "Height - Case Default"


        left_x = [int(cluster_centers[i][0] - widths[i]/2) for i in range(0,n_clusters)]
        left_y = [int(cluster_centers[i][1] - heights[i]/2) for i in range(0,n_clusters)]

        # Draw Rectangles
        for i in range(0,len(left_x)):
            cv2.rectangle(image, (left_x[i],left_y[i]),(left_x[i]+widths[i],left_y[i]+heights[i]), (0, 255, 0), 2)

        plt.show()

        print "Left Points x: ", left_x
        print "Left Points y: ", left_y
        print "Widths ", widths
        print "Heights: ", heights
        print "Image width and height: ", image.shape[1],image.shape[0]
        return left_x, left_y, widths, heights

    def getNumberOfObjects(self):
        return self.n

    def getObjects(self):
        return self.startingPosX, self.startingPosY, self.widths, self.heights

