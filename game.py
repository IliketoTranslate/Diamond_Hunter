import pygame as pg
pg.init()

sc_width = 1800
sc_height = 900
wn = pg.display.set_mode((sc_width, sc_height))

class Player():
    def __init__(self) -> None:
        self.pos_x = 880
        self.pos_y = 855
        self.speed = 3
        self.width = 20
        self.height = 40
        self.hitbox = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.last_key = 0
    def move_up(self):
        self.pos_y -= self.speed
    def move_down(self):
        self.pos_y += self.speed
    def move_left(self):
        self.pos_x -= self.speed
    def move_rigth(self):
        self.pos_x += self.speed
    def move(self, rect):
        keys = pg.key.get_pressed()
        if not(self.hitbox.colliderect(rect)):
            if not(self.pos_y < 10):
                if keys[pg.K_w]:
                    self.move_up()
                    self.last_key = "w"
            if not(self.pos_x < 10):
                if keys[pg.K_a]:
                    self.move_left()
                    self.last_key = "a"
            if not(self.pos_y > 850):
                if keys[pg.K_s]:
                    self.move_down()
                    self.last_key = "s"
            if not(self.pos_x > 1770):
                if keys[pg.K_d]:
                    self.move_rigth()
                    self.last_key = "d"
        else:
            if self.last_key == "w":
                self.move_down()
            if self.last_key == "a":
                self.move_rigth()
            if self.last_key == "s":
                self.move_up()
            if self.last_key == "d":
                self.move_left()
            
        #print("position x = " + str(self.pos_x) + " position y = " + str(self.pos_y)) 
    def draw(self):
        self.hitbox = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        pg.draw.rect(wn, (255, 255, 255), self.hitbox)
    def getRect(self):
        return self.hitbox

class ATM():
    def __init__(self) -> None:
        self.pos_x = 10
        self.width = 40
        self.height = 100
        self.pos_y = sc_height - self.height - 5
        self.hitbox = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.amount_money = 0
        self.last_ammn = 0
    def draw(self):
        self.hitbox = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        pg.draw.rect(wn, (255, 255, 255), self.hitbox)
    def turnSintoM(self, slimes):
        self.amount_money = slimes * 2
        return self.amount_money

class Plate():
    def __init__(self, x, y, type, price) -> None:
        self.pos_x = x
        self.pos_y = y
        self.pos_x2 = x
        self.pos_y2 = y
        self.price = price
        self.is_pressed = False
        self.type = type
        self.width = 30
        self.height = 10
        self.hitbox = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        self.append = 0
    def draw(self):
        self.hitbox = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        pg.draw.rect(wn, (100, 10, 10), self.hitbox)
    def checkIsPressed(self, rect):
        number = 0
        if self.hitbox.colliderect(rect):
            self.is_pressed = True
            self.height = 5
            self.append = 1
        else:
            self.is_pressed = False
            self.height = 10
            self.append = -4
        number = self.pos_y2 + self.append
        self.pos_y = number
    def getIsPressed(self):
        return self.is_pressed
    def getType(self):
        return self.type
    def getPos(self):
        return self.pos_x, self.pos_y
    def getPrice(self):
        return self.price

class SlimeFactory():
    def __init__(self, posx, width, height) -> None:
        self.factory_speed = 1
        self.factory_pos_x = posx
        self.factory_pos_y = sc_height - height - 5
        self.factory_witdh = width
        self.factory_height = height
        self.slime_pos_x = self.factory_pos_x + self.factory_witdh - 20
        self.slime_pos_y = self.factory_pos_y - 15
        self.slime_width = 15
        self.slime_height = self.slime_width
        self.factory_hitbox = pg.rect.Rect(self.factory_pos_x, self.factory_pos_y, self.factory_witdh, self.factory_height)
        self.slime_hitbox = pg.rect.Rect(self.slime_pos_x, self.slime_pos_y, self.slime_width, self.slime_height)
        self.slime_road_x = self.factory_witdh - 20
        self.slime_road_y = self.factory_height
        self.amount_slime = 0
    def draw(self):
        self.factory_hitbox = pg.rect.Rect(self.factory_pos_x, self.factory_pos_y, self.factory_witdh, self.factory_height)      
        self.slime_hitbox = pg.rect.Rect(self.slime_pos_x, self.slime_pos_y, 15, 15)
        pg.draw.rect(wn, (200, 200, 210), self.factory_hitbox)
        pg.draw.rect(wn, (10, 200, 100), self.slime_hitbox)
    def move_slime(self):
        if not(self.slime_road_x < -15):
            self.slime_pos_x -= self.factory_speed
            self.slime_road_x -= self.factory_speed
        elif not(self.slime_road_y < 1):
            self.slime_pos_y += self.factory_speed
            self.slime_road_y -= self.factory_speed
        if self.slime_pos_x <= self.factory_pos_x - 10 and self.slime_pos_y >= self.factory_pos_y + self.factory_height - self.slime_height:
            self.slime_pos_x = self.factory_pos_x + self.factory_witdh - 20
            self.slime_pos_y = self.factory_pos_y - 15
            self.slime_road_x = self.factory_witdh - 20
            self.slime_road_y = self.factory_height
            self.amount_slime += 1
    def resetAmsl(self):
        self.amount_slime = 0
    def getAmountSlime(self):
        return self.amount_slime

class Text():
    def __init__(self, x, y, text, color) -> None:
        self.pos_x = x
        self.pos_y = y
        self.text = text
        self.color = color
        self.font = pg.font.SysFont("Calibri", 48)
        self.wrtx = pg.font.Font.render(self.font, self.text, True, self.color)
    def drawTextVar(self, text):
        self.text = text
        self.wrtx = pg.font.Font.render(self.font, self.text, True, self.color)
        wn.blit(self.wrtx, (self.pos_x, self.pos_y))
    def getPos(self):
        return self.pos_x, self.pos_y

class Rect():
    def __init__(self, x, y, width, height) -> None:
        self.pos_x = x
        self.pos_y = y
        self.width = width
        self.height = height
        self.rect = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
    def draw(self):
        self.rect = pg.rect.Rect(self.pos_x, self.pos_y, self.width, self.height)
        pg.draw.rect(wn, (100, 100, 100), self.rect)
    def getRect(self):
        return self.rect

atm = ATM()
player = Player()

class Main():
    def __init__(self) -> None:
        self.money = 0
        self.factories = list()
        self.texts = list()
        self.plates = list()
        self.rects = list()
        self.ATM_is_pressed = False
        self.test = None
        self.amsl = 0
        self.rect = 0

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
            rect2 = rect.getRect()
            player.move(rect2)
    def getRect(self):
        return self.rect
main = Main()
clock = pg.time.Clock()
run = True
while run:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    bg_color = (0,0,0)
    wn.fill(bg_color)

    #rect = main.getRect()
    main.ATMFunc()
    main.PlateFunc()
    main.SlimeFactoriesStart()
    main.TextFunc()
    main.RectFunc()
    player.draw()

    pg.display.update()