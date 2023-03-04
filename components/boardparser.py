from . import object

class Boardparser():
    def __init__(self, shift, file):
        self._objects = list()
        self._file = file
        self.pos_x = 0
        self.pos_y = 48
        self._shift = shift
        self.parseFile()

    def parseFile(self):
        try: 
            with open(self._file, 'r') as infile:
                for line in infile:
                    for character in line:
                        if character == '#':
                            self._objects.append(object.Mud(self.pos_x, self.pos_y, self._shift))
                        elif character == 'R':
                            self._objects.append(object.Stone(self.pos_x, self.pos_y, self._shift))
                        elif character == 'W':
                            self._objects.append(object.Wall(self.pos_x, self.pos_y, self._shift))
                        elif character == 'P':
                            self._objects.append(object.Player(self.pos_x, self.pos_y, self._shift))
                        elif character == 'D':
                            self._objects.append(object.Diamond(self.pos_x, self.pos_y, self._shift))
                        elif character == 'E':
                            self._objects.append(object.Exit(self.pos_x, self.pos_y, self._shift))
                        self.pos_x += self._shift
                    self.pos_x = 0
                    self.pos_y += self._shift
        except FileNotFoundError:
            print("File not found "+self._file)

    def generateObjects(self):
        for el in self._objects:
            yield el


