
import os
import cv2

from matplotlib import pyplot as plt


class VideoCapture:

    video = 0

    def __init__(self, image):
        pass

    def captureVideo(self):
        path = os.getcwd()+"\..\Data\ideo1.avi"
        # If reading from camera, set path to 0.
        self.video = cv2.VideoCapture(path)

    def readFrames(self):
        if (self.video.isOpened()):
            print "Video source is openeded. Now, it will start reading."

            while(1):
                print "Inside while loop of removeBackground()"
                ret, frame = self.video.read()
                print "Return: ", ret

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                plt.imshow(gray)

                plt.show()

                print "After showing image: "
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    print "Breaking from while loop"
                    break

            self.video.release()
            cv2.destroyAllWindows()

        else:
            print "Video source couldn't be opened"
