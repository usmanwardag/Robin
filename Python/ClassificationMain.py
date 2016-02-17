
import os
from os import path
import sys
import ObjectClassification as classification
from matplotlib import pyplot as plt
import ObjectMapping as mapping

sys.path.insert(0, path.abspath('..'))

def main():
    path_original = os.getcwd()+"\Data\imageMatching03.jpg"
    path_ref = os.getcwd()+"\Data\imageMatching02.jpg"

    image_original = plt.imread(path_original,0)
    image_ref = plt.imread(path_ref,0)
    print "Done loading images"

    object_mapping = mapping.ObjectMapping(image_original)
    print "Created ObjectMapping object"

    object_mapping.mapObjects()
    print "Done Mapping images"

    x_pos, y_pos, widths, heights = object_mapping.getObjects()
    print "Loaded positions"
    print "--------------------------------------------------------------------"
    print "NOW IN CLASSIFICATION"

    object_classify = classification.ObjectClassification(image_original, x_pos, y_pos,
                                                               widths, heights)

    object_classify.matchImage(image_ref)


if __name__ == '__main__':
    main()
