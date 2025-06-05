import pygame
import math
import random
from source.bullets.star_bullet import StarBullet
from source.charactors import enemy
from source import constant as C

class Spirit6(enemy.Enemy):
    def __init__(self, x, y, target_x, target_y, speed):
        images = []
        temp = pygame.image.load(C.sprite_image)
        for i in range(6, 12):
            image = temp.subsurface(self.get_rect(i, 0))
            flipped_image = pygame.transform.flip(image, True, False)
            images.append(flipped_image)
        super().__init__(x, y, target_x, target_y, 16, images, 200, speed)
        self.timer = pygame.time.get_ticks()
        self.times = 0

    def shooting(self, surface, player_bullets, enemy_bullets, player_x=0, player_y=0):
        super().update(surface, player_bullets)
        if pygame.time.get_ticks() - self.timer >= 50:
            self.timer = pygame.time.get_ticks()
            self.times += 1
        if self.times == 30:
            self.times = 0
            # 向玩家发射弹幕
            angle_to_player = math.degrees(math.atan2(player_y - self.y, player_x - self.x))
            enemy_bullets.append(StarBullet(self.x, self.y, angle_to_player, 3))

            # 向随机角度发射弧形弹幕集合
            random_angle = random.uniform(0, 360)
            for i in range(-2, 3):  # 发射5个子弹，形成弧形
                angle = random_angle + i * 10  # 每个子弹之间的角度差为10度
                enemy_bullets.append(StarBullet(self.x, self.y, angle, 3))

    def get_rect(self, x, y):
        return pygame.Rect((x * 32, y * 32, 32, 32))