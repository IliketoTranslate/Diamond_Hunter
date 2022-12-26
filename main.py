from components import *

atm = ATM()

#zakladam ze Main to game engine
class Main():
    def __init__(self, objects) -> None:
        self.money = 0
        self.factories = list()
        self.texts = list()
        self.plates = list()
        self.rects = list()
        self.ATM_is_pressed = False
        self.test = None
        self.amsl = 0
        self.rect = 0
        self.nextId = 1
        self.objects = objects
        for el in self.objects:
            self.registerObject(el)
        self.collcheck = CollidChecker(self.objects)

        x = 270
        price = 100
        number = 10
        for i in range(number):
            self.addPlate(Plate(x, 889, "factory", price))
            x += 150
            price * 2
        self.addSlimeFactory(SlimeFactory(150, 100, 30))
        self.addPlate(Plate(55, 889, "ATM", 0))
        self.addText(Text(10, 10, "Slimes: ", (100, 100, 100)))
        self.addText(Text(10, 50, "Money: ", (100, 100, 100)))
        self.addRect(Rect(500, 400, 200, 50))
    def addSlimeFactory(self, object):
        self.factories.append(object)
    def removePlate(self, object):
        self.plates.remove(object)
    def addText(self, text):
        self.texts.append(text)
    def addRect(self, object):
        self.rects.append(object)
    def ATMFunc(self):
        atm.draw()
        if self.ATM_is_pressed:
            self.money = self.money + atm.turnSintoM(self.amsl)
            self.amsl = 0
            self.ATM_is_pressed = False
    def addPlate(self, object):
        self.plates.append(object)
    def SlimeFactoriesStart(self):
        for fact in self.factories:
            fact.move_slime()
            fact.draw()              
            amsl = fact.getAmountSlime()
            self.amsl = self.amsl + amsl
            fact.resetAmsl()
    def TextFunc(self):
        for text in self.texts:
            x, y = text.getPos()
            if y == 50: 
                text.drawTextVar("Money: "+ str(self.money))
            if y == 10:
                    text.drawTextVar("Slimes: "+ str(self.amsl))
    def PlateFunc(self, player):
        rect = player.getRect()
        for plate in self.plates:
            plate.checkIsPressed(rect)
            x, y = plate.getPos()
            type_plate = plate.getType()
            price_plate = plate.getPrice()
            plate_is_pressed = plate.getIsPressed()
            if type_plate == "ATM" and plate_is_pressed:
                self.ATM_is_pressed = True
            if type_plate == "factory" and plate_is_pressed and self.money >= price_plate:
                self.addSlimeFactory(SlimeFactory(x + 30, 100, 30))
                self.removePlate(plate)
            plate.draw()
    def RectFunc(self):
        for rect in self.rects:
            rect.draw()
    def getRect(self):
        return self.rect
    def getAllObjects(self) -> list():
        l = list()
        for rect in self.rects:
            l.append(rect)
        return l
    #brakuje game engine, dorzucam tu pseudo-rejestr
    def registerObject(self, object) -> None:
        object.setId(self.nextId)
        self.nextId += 1
    def move(self):
        keys = pg.key.get_pressed()
        new_x =0
        new_y =0
        if keys[pg.K_w]:
            new_y=-1
        if keys[pg.K_a]:
            new_x = -1
        if keys[pg.K_s]:
            new_y = 1
        if keys[pg.K_d]:
            new_x = 1
        for el in self.objects:
            if el.is_playable():
                _, coord = el.getRect()
                new_x *= el.get_speed()
                new_y *= el.get_speed()
                if not(self.collcheck.checkCollision(el, (new_x, new_y))):
                    el.update(new_x, new_y)

            if el.is_movable():
                el.move()

    def draw(self):
        for el in self.objects:
            color, coord = el.getRect()
            pg.draw.rect(wn, color, coord)

