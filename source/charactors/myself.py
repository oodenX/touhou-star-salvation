import pygame
import math
from .. import constant as C
from .. import tools
from ..bullets.main_bullet import Bullet


class Marisa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.point = pygame.image.load(C.player_point)
        self.image = pygame.image.load(C.player_image) # 32 * 48
        self.bullet_image = C.bullet_image
        self.timer = pygame.time.get_ticks()
        self.rate = 1.0
        self.life = 3
        self.score = 0
        self.spell = 0
        self.power = 2.80
        self.speed = 10
        self.invincibility = False
        self.position_x = 304
        self.position_y = 600
        self.center_x = self.position_x + 16
        self.center_y = self.position_y + 24
        self.bullet_kind = 0
        self.min_x = 0
        self.min_y = 0
        self.max_x = 608  # 640 - 32
        self.max_y = 672  # 720 - 48
        self.bullets = []

    # 人物的动画
    def moving_animation(self, i, keys):
        if keys[pygame.K_LEFT]:
            return pygame.Rect((i * 32, 48, 32, 48))
        elif keys[pygame.K_RIGHT]:
            return pygame.Rect((i * 32, 96, 32, 48))
        else:
            return pygame.Rect((i * 32, 0, 32, 48))

    # 人物移动的方法
    def moving(self, keys):
        op = False
        if keys[pygame.K_LSHIFT]:
            self.rate = 0.5
        else:
            self.rate = 1.0
        if keys[pygame.K_UP]:
            self.position_y -= self.speed * self.rate
            op = True
        if keys[pygame.K_DOWN]:
            self.position_y += self.speed * self.rate
            op = True
        if keys[pygame.K_RIGHT]:
            self.position_x += self.speed * self.rate
            op = True
        if keys[pygame.K_LEFT]:
            self.position_x -= self.speed * self.rate
            op = True
        if op:
            self.center_x = self.position_x + 16
            self.center_y = self.position_y + 24
        self.out_of_bounds()


    # 检查是否出界
    def out_of_bounds(self):
        self.position_x = max(self.min_x, min(self.position_x, self.max_x))
        self.position_y = max(self.min_y, min(self.position_y, self.max_y))

    # 人物的射击方法
    def shooting(self, surface, keys):
        if keys[pygame.K_z]:
            if pygame.time.get_ticks() - self.timer > 180:
                self.timer = pygame.time.get_ticks()
                self.bullet_kind += 1
                power_level = math.floor(self.power)
                if power_level == 1:
                    bullet = Bullet(self.position_x, self.position_y)
                    self.bullets.append(bullet)
                elif power_level == 2:
                    bullet = Bullet(self.position_x - 8, self.position_y)
                    self.bullets.append(bullet)
                    bullet = Bullet(self.position_x + 8, self.position_y)
                    self.bullets.append(bullet)
                elif power_level == 3:
                    bullet = Bullet(self.position_x - 7, self.position_y)
                    self.bullets.append(bullet)
                    bullet = Bullet(self.position_x, self.position_y - 4)
                    self.bullets.append(bullet)
                    bullet = Bullet(self.position_x + 7, self.position_y)
                    self.bullets.append(bullet)
                elif power_level >= 4:
                    bullet = Bullet(self.position_x - 12, self.position_y)
                    self.bullets.append(bullet)
                    bullet = Bullet(self.position_x + 12, self.position_y)
                    self.bullets.append(bullet)
                    bullet = Bullet(self.position_x - 6, self.position_y - 6)
                    self.bullets.append(bullet)
                    bullet = Bullet(self.position_x + 6, self.position_y - 6)
                    self.bullets.append(bullet)
        for bullet in self.bullets:
            if bullet.alive:
                bullet.draw(surface)
            else:
                self.bullets.remove(bullet)

    # 更新人物的方法
    def update(self, surface, keys):
        self.moving(keys)
        self.shooting(surface, keys)
        if self.power > 4.00:
            self.power = 4.00
        if self.power < 1.00:
            self.power = 1.00