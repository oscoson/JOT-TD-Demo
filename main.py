import pygame
from timeit import default_timer as timer
import os
import random

pygame.init()

# Below represents each enemies sprite animations
# Anni Animations
anniDown = []
anniLeft = []
anniRight = []
anniUp = []
# Baba Animations
babaDown = []
babaLeft = []
babaRight = []
babaUp = []
# Keke Animations
kekeDown = []
kekeLeft = []
kekeRight = []
kekeUp = []
# me Animations
meDown = []
meLeft = []
meRight = []
meUp = []
# Robo Animations
roboDown = []
roboLeft = []
roboRight = []
roboUp = []

counter = 0
loopNum = 0
images = os.listdir("baba cut sprites")
for i in images:
    if loopNum == 0:
        anniDown.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 1:
        anniLeft.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 2:
        anniRight.append(
            pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 3:
        anniUp.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 4:
        babaDown.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 5:
        babaLeft.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 6:
        babaRight.append(
            pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 7:
        babaUp.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 8:
        kekeDown.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 9:
        kekeLeft.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 10:
        kekeRight.append(
            pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 11:
        kekeUp.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 12:
        meDown.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 13:
        meLeft.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 14:
        meRight.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 15:
        meUp.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 16:
        roboDown.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 17:
        roboLeft.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    elif loopNum == 18:
        roboRight.append(
            pygame.image.load(os.path.join("baba cut sprites", i)))
    else:
        roboUp.append(pygame.image.load(os.path.join("baba cut sprites", i)))
    counter += 1
    if counter >= 12:
        loopNum += 1
        counter = 0

displayHeight = 720
displayLength = 1280

win = pygame.display.set_mode((displayLength, displayHeight))

pygame.display.set_caption("JOT TD GAME")
font = pygame.font.SysFont("elephant", 50)
gameOverFont = pygame.font.SysFont("elephant", 100)
heartPic = pygame.image.load("heart.png")
heartPic = pygame.transform.scale(heartPic, (63, 63))
moneyPic = pygame.image.load("money.png")
moneyPic = pygame.transform.scale(moneyPic, (63, 63))


class Button:
    """
    Button class for menu objects
    """

    def __init__(self, menu, img, name):
        self.name = name
        self.img = img
        self.x = menu.x - 50
        self.y = menu.y - 110
        self.menu = menu
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def click(self, X, Y):
        """
        returns if the positon has collided with the menu
        :param X: int
        :param Y: int
        :return: bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:

                return True
        return False

    def draw(self, win):
        """
        draws the button image
        :param win: surface
        :return: None
        """
        win.blit(self.img, (self.x, self.y))

    def update(self):
        """
        updates button position
        :return: None
        """
        self.x = self.menu.x - 50
        self.y = self.menu.y - 110


class PlayPauseButton(Button):
    def __init__(self, play_img, pause_img, x, y):
        self.img = play_img
        self.play = play_img
        self.pause = pause_img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.paused = True

    def draw(self, win):
        if self.paused:
            win.blit(self.play, (self.x, self.y))
        else:
            win.blit(self.pause, (self.x, self.y))


class VerticalButton(Button):
    """
    Button class for menu objects
    """

    def __init__(self, x, y,img, name, cost, tower):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.cost = cost
        self.tower = tower
        self.x = self.tower.x
        self.y = self.tower.y
        self.w = self.tower.w
        self.l = self.tower.l
        self.towerName = self.tower.name
        self.towerImg = self.tower.img
        self.towerRadius = self.tower.radius
        self.towerCost = self.tower.cost
        self.towerDamage = self.tower.damage
        self.towerDmgBoost = self.tower.dmgBoost
        self.towerSpeedBoost = self.tower.speedBoost
        self.towerAttackSpeed = self.tower.attackSpeed
        self.towerExplosions = self.tower.explosions
        


class Menu:
    """
    menu for holding items
    """

    def __init__(self, tower, x, y, img, item_cost):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.item_cost = item_cost
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.SysFont("comicsans", 25)
        self.tower = tower

    def add_btn(self, img, name):
        """
        adds buttons to menu
        :param img: surface
        :param name: str
        :return: None
        """
        self.items += 1
        self.buttons.append(Button(self, img, name))

    def get_item_cost(self):
        """
        gets cost of upgrade to next level
        :return: int
        """
        return self.item_cost[self.tower.level - 1]

    def draw(self, win):
        """
        draws btns and menu bg
        :param win: surface
        :return: None
        """
        win.blit(self.bg, (self.x - self.bg.get_width() // 2, self.y - 120))
        for item in self.buttons:
            item.draw(win)
            text = self.font.render(
                str(self.item_cost[self.tower.level - 1]), 1, (255, 255, 255))
            win.blit(text, (item.x + item.width + 30 - text.get_width() // 2,
                            item.y + moneyPic.get_height() - 8))

    def get_clicked(self, X, Y):
        """
        return the clicked item from the menu
        :param X: int
        :param Y: int
        :return: str
        """
        for btn in self.buttons:
            if btn.click(X, Y):
                return btn.name

        return None

    def update(self):
        """
        update menu and button location
        :return: None
        """
        for btn in self.buttons:
            btn.update()


class VerticalMenu(Menu):
    """
    Vertical Menu for side bar of game
    """

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.SysFont("comicsans", 25)

    def add_btn(self, btn_x, btn_y, img, name, cost, tower):
        """
        adds buttons to menu
        :param img: surface
        :param name: str
        :return: None
        """
        self.items += 1
        self.buttons.append(
            VerticalButton(btn_x, btn_y, img, name, cost, tower))

    def get_item_cost(self, name):
        """
        gets cost of item
        :param name: str
        :return: int
        """
        for btn in self.buttons:
            if btn.name == name:
                return btn.cost
        return -1

    def draw(self, win):
        """
        draws btns and menu bg
        :param win: surface
        :return: None
        """
        win.blit(self.bg, (self.x, self.y))
        for item in self.buttons:
            item.draw(win)
            text = self.font.render(str(item.cost), 1, (255, 255, 255))
            win.blit(text,
                     (item.x + item.width // 2 - text.get_width() // 2 + 7,
                      item.y + item.height + 5))


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)


towerClicked = False

radiusImg = pygame.image.load('radius.png')


class Tower:
    def __init__(self,x,y,w,l,name,explosions,img,radius,cost,damage=1,dmgBoost=0,speedBoost=0,attackDelay=1,placed=False,specialTraits=[]):  # add to it
        self.img = img
        self.radius = radius
        self.radiusImg = pygame.transform.scale(radiusImg,
                                                (self.radius, self.radius))
        self.cost = cost
        self.name = name
        self.damage = damage
        self.minimumWave = 0
        self.speedBoost = speedBoost
        self.dmgBoost = dmgBoost
        self.sellCost = int(cost * 0.8)
        self.attackSpeed = attackDelay
        self.clicked = False
        self.placed = placed
        self.x = x
        self.y = y
        self.w = w
        self.l = l
        self.startX = x
        self.startY = y
        self.rect = pygame.Rect(x, y, w, l)
        self.mousedown = False
        self.default = self
        self.imgName = img
        self.inPath = False
        self.inTower = False
        self.delay = attackDelay
        self.cooldown = 0
        self.explosions = explosions
        self.hasExplosion = False
        

    def placeTower(self, event, path):
        global towerClicked, towers
        if self.clicked and not self.placed:
            self.x, self.y = pygame.mouse.get_pos()
            self.x = self.x - 20
            self.y = self.y - 20
            self.rect = pygame.Rect(self.x, self.y, self.w, self.l)

        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.rect.collidepoint(event.pos):
                if not self.placed and not self.clicked and not towerClicked:
                    self.clicked = True
                    towerClicked = True
                    self.mousedown = True

                if not self.clicked and not self.placed:
                    self.clicked = True

                for p in path:
                    if self.rect.colliderect(p):
                        self.inPath = True
                for t in towers:
                    if self.rect.colliderect(t.rect) and t != self:
                        self.inTower = True
                if not self.placed and self.clicked and self.y <= 430 and not self.mousedown and not self.inPath and not self.inTower:
                    self.clicked = False
                    self.placed = True
                    towerClicked = False
                    towers.append(
                        Tower(self.startX, self.startY, self.w, self.l,
                              self.name, self.imgName, self.radius, self.cost,
                              self.damage, self.dmgBoost, self.speedBoost,
                              self.attackSpeed, self.minimumWave))
                self.inTower = False
                self.inPath = False
                if not self.placed and self.clicked and self.y > 430 and not self.mousedown:
                    self.clicked = False
                    self.placed = False
                    towerClicked = False
                    self.x, self.y = self.startX, self.startY
                    self.rect = pygame.Rect(self.x, self.y, self.w, self.l)
            self.mousedown = True
        else:
            self.mousedown = False
    def target(self, enemies):
        if self.cooldown:
            self.cooldown -= 1
        elif enemies:
            greatestPath = 0
            group = []
            for en in enemies:
                if en.pathNum > greatestPath:
                    group = []
                    group.append(en)
                    greatestPath = en.pathNum
                elif en.pathNum == greatestPath:
                    group.append(en)

            smallest = 1000000
            location = (self.x+(self.w//2), self.y+(self.l//2))
            farthest = []
            for en in group:
                xdist = abs(en.x - location[0])
                ydist = abs(en.y - location[1])
                if  xdist < self.radius and ydist < self.radius:
                    distance = abs(en.distance[0]) + abs(en.distance[1])
                    if distance < smallest:
                        smallest = distance
                        farthest = en
            if farthest:
                farthest.health -= self.damage
            self.cooldown = self.delay
                


    def draw(self):
        global radius
        if self.clicked:
            w = self.radiusImg.get_width() / 2 - self.w / 2
            l = self.radiusImg.get_height() / 2 - self.l / 2
            blit_alpha(win, self.radiusImg, (self.x - w, self.y - l), 128)
        win.blit(self.img, (self.x, self.y))


class Enemy:  # Enemy Units
    def __init__(self, width, height, health, attack, speed, loot, downPics,
                 leftPics, rightPics, upPics):
        self.x = 151
        self.y = 0
        self.rightPics = rightPics
        self.leftPics = leftPics
        self.upPics = upPics
        self.downPics = downPics
        self.health = health
        self.loot = loot
        self.path = [(152, 8), (150, 176), (248, 177), (246, 304), (389, 303),
                     (392, 344), (440, 346), (439, 597),
                     (391, 595), (389, 639), (104, 636), (103, 597), (54, 595),
                     (55, 344), (101, 343), (104, 303), (392, 302), (394, 344),
                     (440, 346), (438, 512), (631, 511), (632, 596), (824,
                                                                      595),
                     (823, 347), (958, 345)]
        self.attack = attack  # lives lost
        self.animationCount = 0
        self.width = width
        self.height = height
        self.pathNum = 0
        self.distance = ((self.path[self.pathNum][0] - self.x),
                         self.path[self.pathNum][1] - self.y)
        self.direction = (self.distance[0] // abs(self.distance[0]),
                          self.distance[0] // abs(self.distance[0]))
        self.speed = speed
        self.past = False
        self.DED = False
        self.maxHealth = health

    def draw(self, win, images):
        self.animationCount += 1
        if self.animationCount > 44:
            self.animationCount = 0
        win.blit(images[self.animationCount // 4], (self.x, self.y))
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y - 5, self.width, 5))
        pygame.draw.rect(win, (0, 255, 0),
                         (self.x, self.y - 5,
                          round(self.width * (self.health / self.maxHealth)), 5))

    def collide(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.x + self.width and Y > self.y:
                return True

    def move(self):
        if abs(self.distance[0]) >= abs(self.distance[1]) and not (
                self.distance[0] * self.direction[0] <= 0):
            self.x += self.speed * self.direction[0]
            if self.direction[0] > 0:
                self.draw(win, self.rightPics)
            else:
                self.draw(win, self.leftPics)

        elif not (self.distance[1] * self.direction[1] <= 0):
            self.y += self.speed * self.direction[1]
            if self.direction[1] > 0:
                self.draw(win, self.downPics)
            else:
                self.draw(win, self.upPics)

        else:
            self.x += self.speed * self.direction[0]
            if self.direction[0] > 0:
                self.draw(win, self.rightPics)
            else:
                self.draw(win, self.leftPics)
        self.distance = (self.path[self.pathNum][0] - self.x,
                         self.path[self.pathNum][1] - self.y)
        if self.distance[0] * self.direction[0] <= 0 and self.distance[
                1] * self.direction[1] <= 0:
            self.pathNum += 1
            if self.pathNum < len(self.path):
                self.distance = (self.path[self.pathNum][0] - self.x,
                                 self.path[self.pathNum][1] - self.y)
                if self.x == self.path[self.pathNum][0]:
                    if self.y == self.path[self.pathNum][1]:
                        self.direction = (0, 0)
                    else:
                        self.direction = (
                            0, self.distance[1] // abs(self.distance[1]))
                elif self.y == self.path[self.pathNum][1]:
                    self.direction = (
                        self.distance[0] // abs(self.distance[0]), 0)
                else:
                    self.direction = (
                        self.distance[0] // abs(self.distance[0]),
                        self.distance[1] // abs(self.distance[1]))
            else:
                self.past = True

    def hit(self):
        pass


anni = Enemy(30, 30, 30, 5, 6, 5, anniDown, anniLeft, anniRight, anniUp)
baba = Enemy(30, 30, 60, 10, 4, 20, babaDown, babaLeft, babaRight, babaUp)
keke = Enemy(30, 30, 90, 15, 3, 20, kekeDown, kekeLeft, kekeRight, kekeUp)
me = Enemy(30, 30, 30, 5, 2, 10, meDown, meLeft, meRight, meUp)
robo = Enemy(30, 30, 600, 25, 1, 50, roboDown, roboLeft, roboRight, roboUp)

sideBar = VerticalMenu(
    961, 0, pygame.transform.scale(
        pygame.image.load("scroll.png"), (320, 720)))
fireLauncher = pygame.transform.scale(
    pygame.image.load(os.path.join("Tower Sprites", "Fire Launcher 1.png")),
    (110, 110))

boulderLauncher = pygame.transform.scale(
    pygame.image.load(os.path.join("Tower Sprites", "Boulder Launcher 1.png")),
    (110, 110))
rockLauncher = pygame.transform.scale(
    pygame.image.load(os.path.join("Tower Sprites", "Rock Launcher 1.png")),
    (110, 110))
spikedLauncher = pygame.transform.scale(
    pygame.image.load(os.path.join("Tower Sprites", "Spiked Launcher 1.png")),
    (110, 110))

RockExplosion = []
FireExplosion = []
SpikeExplosion = []
BoulderExplosion = []
for x in range(54,62):
    FireExplosion.append(
        pygame.transform.scale(pygame.image.load(os.path.join("Explosions", str(x) + ".png")),(45,45)).convert_alpha())

for x in range(45,49):
    BoulderExplosion.append(
        pygame.transform.scale(pygame.image.load(os.path.join("Explosions", str(x) + ".png")),(45,45)).convert_alpha())

for x in range(40,45):
    SpikeExplosion.append(
        pygame.transform.scale(pygame.image.load(os.path.join("Explosions", str(x) + ".png")),(45,45)).convert_alpha())

for x in range(29,35):
    RockExplosion.append(
        pygame.transform.scale(pygame.image.load(os.path.join("Explosions", str(x) + ".png")),(45,45)).convert_alpha())

sideBar.add_btn(
    1055, 220, fireLauncher, "test", 200,
    Tower(1055, 220, 110, 110, 'FireLauncher',FireExplosion, fireLauncher, 150, 200, 15, 0,
          0, 85, False))

sideBar.add_btn(
    1055, 70, boulderLauncher, "test", 300,
    Tower(1055, 70, 110, 110, 'BoulderLauncher',BoulderExplosion, boulderLauncher, 200, 300, 30,
          0, 0, 130, False))

sideBar.add_btn(
    1055, 370, rockLauncher, "test", 100,
    Tower(1055, 370, 110, 110, 'RockLauncher',RockExplosion, rockLauncher, 200, 100, 7, 0,
          0, 40, False))

sideBar.add_btn(
    1055, 520, spikedLauncher, "test", 150,
    Tower(1055, 520, 110, 110, 'SpikedLauncher',SpikeExplosion, spikedLauncher, 150, 150, 10,
          0, 0, 60, False))




class Level:  # Currently represents our first level. Can be used as the base for future levels
    def __init__(self):  # Initialization of base game elements
        self.width = 1280
        self.height = 720
        self.win = pygame.display.set_mode((self.width, self.height))
        self.multiwave = []
        self.waveCount = 1
        self.wave = [me]
        self.enemyDelay = [
            random.randint(0, 1500) for i in range(len(self.wave))
        ]
        self.enemies = []
        self.towers = []
        self.lives = 100
        self.money = 150
        self.background = pygame.transform.scale(
            pygame.image.load("loop background.jpg"), (960, 720))
        self.clicks = []
        self.path = [(152, 8), (150, 176), (248, 177), (246, 304), (389, 303),
                     (392, 344), (440, 346), (439, 597),
                     (391, 595), (389, 639), (104, 636), (103, 597), (54, 595),
                     (55, 344), (101, 343), (104, 303), (392, 302), (394, 344),
                     (440, 346), (438, 512), (631, 511), (632, 596), (824,
                                                                      595),
                     (823, 347), (958, 345)]
        self.holding = False

    def newWave(self):
        self.waveCount += 1
        self.wave = []
        for i in range(self.waveCount):
            self.wave.append(
                Enemy(30, 30, 10+self.waveCount, 5, 2, 7, meDown, meLeft, meRight, meUp))
        for i in range(self.waveCount // 2):
            self.wave.append(
                Enemy(30, 30, 20+(self.waveCount*2), 15, 3, 15, kekeDown, kekeLeft, kekeRight,
                      kekeUp))
        for i in range(self.waveCount // 3):
            self.wave.append(
                Enemy(30, 30, 30+(self.waveCount*3), 10, 4, 15, babaDown, babaLeft, babaRight,
                      babaUp))
        for i in range(self.waveCount // 4):
            self.wave.append(
                Enemy(30, 30, 1+(self.waveCount*4), 5, 6, 5, anniDown, anniLeft, anniRight,
                      anniUp))
        for i in range(self.waveCount // 5):
            self.wave.append(
                Enemy(30, 30, 60+(self.waveCount*5), 25, 1, 35, roboDown, roboLeft, roboRight,
                      roboUp))
        random.shuffle(self.wave)
        self.enemyDelay = [
            random.randint(0, 1500 - (self.waveCount * 10))
            for i in range(len(self.wave))
        ]

    def run(
            self
    ):  # function for running the game and starting the waves. Includes the basic timers for waves, the starttime and endtime. Enables the ability to quit
        run = True
        fps = pygame.time.Clock()
        startTime = int(round(timer() * 1000))
        endTime = int(round(timer() * 1000))
        while run:
            fps.tick(30)
            if (self.wave and self.enemyDelay
                ) and endTime - startTime >= self.enemyDelay[0]:
                startTime = int(round(timer() * 1000))
                self.enemies.append(self.wave.pop(0))
                self.enemyDelay.pop(0)
            if not (self.enemies) and not (self.wave):
                self.newWave()
                self.money += 75
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                position = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in sideBar.buttons:
                        if i.click(position[0],
                                position[1]) and not (self.holding):
                            if self.money >= i.cost:
                                new = Tower(i.x,i.y,i.w,i.l,i.towerName,i.towerExplosions,i.towerImg,i.towerRadius,i.towerCost,i.towerDamage,i.towerDmgBoost,i.towerSpeedBoost,i.towerAttackSpeed)
                                self.towers.append(new)
                                self.holding = True
            for tow in self.towers:
                if tow.placed:
                    tow.target(self.enemies)
            temp = []
            for en in self.enemies:
                if not (en.past):
                    if en.health < 1:
                        self.money += en.loot
                    else:
                        temp.append(en)

                else:
                    self.lives -= en.attack

            self.enemies = temp
            self.draw()
            endTime = int(round(timer() * 1000))
            if self.lives < 1:
                gameOver = gameOverFont.render("GAME OVER", 1, (255, 0, 0))
                win.blit(gameOver, ((1280 - gameOver.get_width()) // 2,
                                    (720 - gameOver.get_height()) // 2))
                pygame.display.update()
                pygame.time.delay(500)
                pygame.quit()
        pygame.quit()

    def draw(
            self
    ):  # allows the user to draw dots onto the screen -> an aid to see where the points can be made for the path
        pygame.draw.rect(win, (0, 0, 0), (0, 0, 1280, 720))
        self.win.blit(self.background, (0, 0))
        for en in self.enemies:
            en.move()
        
        win.blit(heartPic, (0, 0))
        lifeText = font.render(str(self.lives), 1, (255, 255, 255))
        win.blit(moneyPic, (175, 0))
        win.blit(lifeText, (63, 0))
        moneyText = font.render(str(self.money), 1, (255, 255, 255))
        win.blit(moneyText, (238, 0))
        waveText = font.render("Wave #" + str(self.waveCount), 1, (255, 255, 255))
        win.blit(waveText,(670,0))
        sideBar.draw(win)
        for tow in self.towers:
            if not(tow.placed):
                tow.x, tow.y = pygame.mouse.get_pos()
                if tow.x < 940 and tow.y < 700:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.money -= tow.cost
                            tow.placed = True
                            self.holding = False
            tow.draw()
        pygame.display.update()


RockExplosion = []
FireExplosion = []
SpikeExplosion = []
BoulderExplosion = []
for x in range(54,62):
    FireExplosion.append(
        pygame.image.load(os.path.join("Explosions", str(x) + ".png")).convert_alpha())

for x in range(45,49):
    BoulderExplosion.append(
        pygame.image.load(os.path.join("Explosions", str(x) + ".png")).convert_alpha())

for x in range(40,45):
    SpikeExplosion.append(
        pygame.image.load(os.path.join("Explosions", str(x) + ".png")).convert_alpha())

for x in range(29,35):
    RockExplosion.append(
        pygame.image.load(os.path.join("Explosions", str(x) + ".png")).convert_alpha())


g = Level()
g.run()
