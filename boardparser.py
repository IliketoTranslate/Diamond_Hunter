import object

class Boardparser():
    def __init__(self):
        pass

    def generateObjects(self):
        objects = list()
        objects.append(object.Mud(0,0))
        objects.append(object.Stone(100,100))

        for el in objects:
            yield el


