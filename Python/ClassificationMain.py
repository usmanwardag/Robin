import cv2
import os
import sys
from matplotlib import pyplot as plt
import time

import ObjectClassification as classification
import ObjectMapping as mapping


def main():
    start = time.time()
    path_original = os.getcwd()+"\Data\imageMatching03.jpg"
    path_ref = os.getcwd()+"\Data\imageMatching02.jpg"

    image_original = plt.imread(path_original,0)

    # Resize image maintaining the aspect ratio
    r = 400.0 / image_original.shape[1]
    image_resized = resizeImage(image_original,400,int(image_original.shape[0] * r))

    image_ref = plt.imread(path_ref,0)
    print "Done loading images"

    object_mapping = mapping.ObjectMapping(image_resized)
    print "Created ObjectMapping object"

    object_mapping.mapObjects()
    print "Done Mapping images"

    x_pos, y_pos, widths, heights = object_mapping.getObjects()
    print "Loaded positions"
    print "--------------------------------------------------------------------"
    print "NOW IN CLASSIFICATION"

    object_classify = classification.ObjectClassification(image_resized, x_pos, y_pos,
                                                               widths, heights)

    matches = object_classify.findImage(image_ref)

    # Draw Rectangles
    for i in range(0,len(x_pos)):
        plt.imshow(image_resized)
        cv2.rectangle(image_resized, (x_pos[i],y_pos[i]),(x_pos[i]+widths[i],y_pos[i]+heights[i]), (0, 255, 0), 2)

        if matches[i]:

            print "Good match found!"
            match_pos = [x_pos[i]+widths[i]/2, y_pos[i]+heights[i]/2]

            # Write text indicating match found
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image_resized,'Matched!',(x_pos[i],y_pos[i]+heights[i]/2),
                        font, 0.5,(0,0,255),1)

    plt.show()

def resizeImage(image, xPixels, yPixels):
    return cv2.resize(image,(xPixels,yPixels))


if __name__ == '__main__':
    main()
