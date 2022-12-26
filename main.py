from components.slimefac import SlimeFactory
from components.utils import Text, Rect
from components.plate import Plate
from components.atm import ATM
from components.player import Player
from components.defs import sc_width, sc_height, wn

atm = ATM()

class Main():
    def __init__(self, player) -> None:
        self.money = 0
        self.factories = list()
        self.texts = list()
        self.plates = list()
        self.rects = list()
        self.ATM_is_pressed = False
        self.test = None
        self.amsl = 0
        self.rect = 0
        self.player = player

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
    def PlateFunc(self):
        rect = self.player.getRect()
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
            rect2 = rect.getRect()
            self.player.move(rect2)
    def getRect(self):
        return self.rect
