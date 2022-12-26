import pygame

window = pygame.display.set_mode((1720, 980))
pygame.init()

bottle = pygame.image.load("bottle.png")
bottle = pygame.transform.scale(bottle, (50, 100))
run = True

class GameEngine:
    def __init__(self) :
        self.enemies = list()
        self.bottles = list()
        self.health = 100
        self.addEnemy(Enemy(self.health))
        self.isLMBPressed = False
        

    def addEnemy(self, enemy):
        self.enemies.append(enemy)

    def addBottle(self, bottle):
        self.bottles.append(bottle)

    def check_events(self) :
        keys = pygame.key.get_pressed()

        if pygame.mouse.get_pressed()[0] and not(self.isLMBPressed):
            x, y = pygame.mouse.get_pos()
            self.bottles.append(Bottle(x, y))
            self.isLMBPressed = True
        elif not(pygame.mouse.get_pressed()[0]):
            self.isLMBPressed = False

    def checkCollides(self):
        for bottle in self.bottles:
            for enemy in self.enemies:
                if enemy.getRect().colliderect(bottle.getRect()):
                    self.bottles.remove(bottle) 
                    enemy.hit()
                    if enemy.getHp() <=0:
                        self.enemies.remove(enemy)
                             
    def main(self):
        self.check_events()
        
        for bottle in self.bottles:
            bottle.draw()
            if bottle.checkDisappear():
                self.bottles.remove(bottle)
        self.checkCollides()

        if not(self.enemies):
            self.health*=2
            self.enemies.append(Enemy(self.health))

        for enemy in self.enemies:
            enemy.draw()

        self.move()

    def move(self):
        for bottle in self.bottles:
            bottle.move()
        for enemy in self.enemies:
            enemy.move()
        
class Enemy :
    def __init__(self, HP) :
        self.cord_x = 100
        self.cord_y = 700
        self.health = HP 
        self.enemyhit = pygame.rect.Rect(self.cord_x, self.cord_y, 100, 200)

    def move(self) :
        if self.cord_x < 1620 :
            self.cord_x += 0.1
        else :
            self.cord_x = 100
    
    def draw(self) :
        self.enemyhit = pygame.rect.Rect(self.cord_x, self.cord_y, 100, 200)
        self.zycie = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 50), f"HP = {self.health}", True, (100, 100, 100))
        window.blit(self.zycie, (self.cord_x, self.cord_y - 60))
        pygame.draw.rect(window, (100, 100, 100), self.enemyhit)

    def hit(self) :
        self.health = self.health - 10

    def getRect(self):
        return self.enemyhit

    def getHp(self):
        return self.health

class Bottle() :
    def __init__(self, x, y) :                                                                           
        self.y_boost = 0.0
        self.x = x
        self.y = y
        self.bottle_hitbox = pygame.rect.Rect(self.x, self.y, 50, 100)

    def move(self) :
        if not (self.y > 880) :
            self.y += self.y_boost
            self.y_boost += 0.02
        
    def draw(self) :
        window.blit(bottle, (self.x, self.y))
        self.bottle_hitbox = pygame.rect.Rect(self.x, self.y, 50, 100)
        if self.y > 880 : 
            self.spadam = False
            self.y_boost = 0

    def checkDisappear(self):
        return self.y > 880

    def getRect(self):
        return self.bottle_hitbox

game = GameEngine()

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # jeśli gracz zamknie okienko
            run = False

    window.fill((0, 0, 0)) 
    game.main()  
    
    pygame.display.update()
