class Tower:

    def __init__(self, image, damage, attack_speed, range):
        """Initializes a new tower instance."""
        super().__init__(image)
        self.damage = damage
        self.attack_speed = attack_speed
        self.range = range

    def draw_placement(self, win):
        # draw range circle
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.place_color, (50, 50), 50, 0)

        win.blit(surface, (self.x - 50, self.y - 50))
    
    def draw(self, win):
        """
        draws the tower
        :param win: surface
        :return: None
        """
        img = self.tower_imgs[self.level - 1]
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))

        # draw menu
        if self.selected:
            self.menu.draw(win)

    def draw_radius(self,win):
        if self.selected:
            # draw range circle
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            win.blit(surface, (self.x - self.range, self.y - self.range))

    def click(self, X, Y):
        """
        returns if tower has been clicked on
        and selects tower if it was clicked
        :param X: int
        :param Y: int
        :return: bool
        """
        img = self.tower_imgs[self.level - 1]
        if X <= self.x - img.get_width() // 2 + self.width and X >= self.x - img.get_width() // 2:
            if Y <= self.y + self.height - img.get_height() // 2 and Y >= self.y - img.get_height() // 2:
                return True
        return False

    def sell(self):
        """
        call to sell the tower, returns sell price
        :return: int
        """
        return self.sell_price[self.level - 1]

    def upgrade(self):
        """
        upgrades the tower for a given cost
        :return: None
        """
        if self.level < len(self.tower_imgs):
            self.level += 1
            self.damage += 1

    def get_upgrade_cost(self):
        """
        returns the upgrade cost, if 0 then can't upgrade anymore
        :return: int
        """
        return self.price[self.level - 1]

    def move(self, x, y):
        """
        moves tower to given x and y
        :param x: int
        :param y: int
        :return: None
        """
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()

    def collide(self, otherTower):
        x2 = otherTower.x
        y2 = otherTower.y

        dis = math.sqrt((x2 - self.x) ** 2 + (y2 - self.y) ** 2)
        if dis >= 100:
            return False
        else:
            return True

    def attack(self, targets):
        """Attempts to attack a target/targets."""
        targets = self._seek_targets(targets)
        if targets:
            self._attack(targets)

    def _attack(self, targets):
        """The actual attacking, deals damage to targets."""
        raise NotImplementedError

    def _seek_targets(self, targets):
        """Seek all possible targets and sort them by distance."""
        targets = (t for t in targets if self.centerdist(t) <= self.range)
        return sorted(targets, key=self.centerdist, reverse=True)


class BoulderTower(Tower):

    def __init__(self):
        """Initializes a new tower."""
        super().__init__(
            image='',
            damage=20,
            attack_speed=1.3,
            range=300
        )

    def _attack(self, targets):
        """Attack multiple targets."""
        main_target = targets[0]
        main_target.take_damage(self.damage)
        splash_dmg = self.damage // 2
        for target in targets[1:]:
            dist = main_target.centerdist(target)
            if dist < 1:
                target.take_damage(splash_dmg)
            elif dist < 300:
                target.take_damage(splash_dmg * (1 / dist))
