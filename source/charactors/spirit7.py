import pygame
import math
import random
from source.bullets.star_bullet import StarBullet
from source.bullets.glowing_bullet import GlowingBullet
from source.charactors import enemy
from source import constant as C

class Spirit7(enemy.Enemy):
    def __init__(self, x, y, target_x, target_y, speed):
        images = []
        temp = pygame.image.load(C.sprite_image)
        for i in range(6, 12):
            image = temp.subsurface(self.get_rect(i, 0))
            images.append(image)
        super().__init__(x, y, target_x, target_y, 16, images, 200, speed)
        self.timer = pygame.time.get_ticks()
        self.move_timer = pygame.time.get_ticks()
        self.times = 0
        self.move_direction = random.choice(['left', 'right', 'up', 'down'])

    def get_rect(self, x, y):
        return pygame.Rect((x * 32, y * 32, 32, 32))

    def move(self):
        if pygame.time.get_ticks() - self.move_timer > 1500:
            self.move_timer = pygame.time.get_ticks()
            self.move_direction = random.choice(['left', 'right', 'up', 'down'])

        if self.move_direction == 'left':
            self.x -= self.speed
        elif self.move_direction == 'right':
            self.x += self.speed
        elif self.move_direction == 'up':
            self.y -= self.speed
        elif self.move_direction == 'down':
            self.y += self.speed

        self.x = max(0, min(self.x, 640 - 32))
        self.y = max(0, min(self.y, 480 - 32))

    def shooting(self, surface, player_bullets, enemy_bullets, player_x=0, player_y=0):
        super().update(surface, player_bullets)
        if pygame.time.get_ticks() - self.timer >= 50:
            self.timer = pygame.time.get_ticks()
            self.times += 1
        if self.times == 30:
            self.times = 0
            for _ in range(10):
                angle = random.uniform(0, 360)
                enemy_bullets.append(GlowingBullet(self.x, self.y, angle, 3))

    def update(self, surface, player_bullets, enemy_bullets, player_x=0, player_y=0):
        self.move()
        self.shooting(surface, player_bullets, enemy_bullets, player_x, player_y)
        image = self.images[self.times % len(self.images)]
        surface.blit(image, (self.x, self.y))