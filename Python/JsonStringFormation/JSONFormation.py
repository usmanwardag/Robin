from json import JSONEncoder
import json

class JSONFormation:

    def __init__(self):
        string1 = self.createObjectJSON(["1", "2", "3", "4", "5"])
        string2 = self.createObjectJSON(["10", "20", "30", "40", "50"])
        strings = [string1, string2]
        frame1 = self.createFrameJSON(strings)
        frame2 = self.createFrameJSON(strings)
        frames = [frame1, frame2]
        self.createVideoJSON(frames)


    def createObjectJSON(self, info_list):

        jsonString = JSONEncoder().encode({
            "Id": info_list[0],
            "Coordinates": info_list[1],
            "Width": info_list[2],
            "Height": info_list[3],
            "Category": info_list[4],
        })

        return jsonString

    def createFrameJSON(self, objectJsonStrings):
        objects = {'Objects': objectJsonStrings}
        frameJsonString = json.dumps(objects)
        return frameJsonString

    def createVideoJSON(self,frameJSONStrings):
        frames = {'Frames': frameJSONStrings}
        videoJSONString = json.dumps(frames)
        print videoJSONString

