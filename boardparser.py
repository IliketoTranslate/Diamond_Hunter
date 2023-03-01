import object

class Boardparser():
    def __init__(self, shift, file):
        self._objects = list()
        self._file = file
        self.pos_x = 0
        self.pos_y = 0
        self._shift = 100
        self.parseFile()

    def parseFile(self):
        try: 
            with open(self._file, 'r') as infile:
                for line in infile:
                    for character in line:
                        if character == '#':
                            self._objects.append(object.Mud(self.pos_x, self.pos_y))
                        elif character == 'S':
                            self._objects.append(object.Stone(self.pos_x, self.pos_y))
                        self.pos_x += self._shift
                    self.pos_x = 0
                    self.pos_y += self._shift
        except FileNotFoundError:
            print("File not found "+self.file)

    def generateObjects(self):
        for el in self._objects:
            yield el


