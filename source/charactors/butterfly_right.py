import pygame
import math
from source.bullets.big_bullet_blue import BigBulletBlue
from source.bullets.big_bullet_yellow import BigBulletYellow
from source.bullets.glowing_bullet import GlowingBullet
from source.bullets.circle_bullet import CircleBullet
from source.charactors import enemy

class ButterflyRight1(enemy.Enemy):
    def __init__(self, x, y, target_x, target_y, speed):
        images = []
        for i in range(1, 6):
            temp = pygame.image.load('./resources/enemy/butterfly_right_' + str(i) + '.png')
            images.append(temp)
        super().__init__(x, y, target_x, target_y, 32, images, 200, speed)
        self.timer = pygame.time.get_ticks()
        self.times = 0

    def shooting(self, surface, player_bullets, enemy_bullets, player_x=0, player_y=0):
        super().update(surface, player_bullets)
        if pygame.time.get_ticks() - self.timer >= 50:
            self.timer = pygame.time.get_ticks()
            self.times += 1

        if self.times == 24:
            self.times = 0
            for angle in range(0, 360, 45):
                enemy_bullets.append(BigBulletYellow(self.x, self.y, angle, 3))

class ButterflyRight2(enemy.Enemy):
    def __init__(self, x, y, target_x, target_y, speed):
        images = []
        for i in range(1, 6):
            temp = pygame.image.load('./resources/enemy/butterfly_right_' + str(i) + '.png')
            images.append(temp)
        super().__init__(x, y, target_x, target_y, 32, images, 200, speed)
        self.timer = pygame.time.get_ticks()
        self.times = 0

    def shooting(self, surface, player_bullets, enemy_bullets, player_x=0, player_y=0):
        super().update(surface, player_bullets)
        if pygame.time.get_ticks() - self.timer >= 50:
            self.timer = pygame.time.get_ticks()
            self.times += 1
        if self.times == 32:
            self.times = 0
            angle = math.degrees(math.atan2(player_y - self.y, player_x - self.x))
            enemy_bullets.append(CircleBullet(self.x, self.y, angle, 3))

class ButterflyRight3(enemy.Enemy):
    def __init__(self, x, y, target_x, target_y, speed):
        images = []
        for i in range(1, 6):
            temp = pygame.image.load('./resources/enemy/butterfly_right_' + str(i) + '.png')
            images.append(temp)
        super().__init__(x, y, target_x, target_y, 32, images, 200, speed)
        self.timer = pygame.time.get_ticks()
        self.times = 0

    def shooting(self, surface, player_bullets, enemy_bullets, player_x=0, player_y=0):
        super().update(surface, player_bullets)
        if pygame.time.get_ticks() - self.timer >= 50:
            self.timer = pygame.time.get_ticks()
            self.times += 1
        if self.times == 32:
            self.times = 0
            angle = math.degrees(math.atan2(player_y - self.y, player_x - self.x))
            enemy_bullets.append(GlowingBullet(self.x, self.y, angle, 3))