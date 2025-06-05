import math

import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y, speed, half_width, radius):
        pygame.sprite.Sprite.__init__(self)
        # 这里的子弹的坐标是子弹正中心的坐标，目标坐标也是目标的正中心坐标
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.speed = speed
        self.half_width = half_width
        self.radius = radius
        self.dx, self.dy = self.calculate_direction()
        self.timer = pygame.time.get_ticks()

    def calculate_direction(self):
        """
        计算子弹移动的方向（x, y分量）
        """
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        distance = math.sqrt(dx**2 + dy**2)
        # 标准化向量，确保速度向量长度等于speed
        dx = dx * (self.speed / distance) if distance != 0 else 0
        dy = dy * (self.speed / distance) if distance != 0 else 0
        return dx, dy

    def out_of_screen(self):
        """
        判断子弹是否飞出屏幕
        """
        return self.x < 0 or self.x > 640 or self.y < 0 or self.y > 720

    def is_hit(self, x, y):
        """
        判断是否击中目标
        """
        return (self.x - x) * (self.x - x) + (self.y - y) * (self.y - y) <= self.radius * self.radius

    def update(self, surface):
        if pygame.time.get_ticks() - self.timer > 10:
            self.x += self.dx
            self.y += self.dy
            self.timer = pygame.time.get_ticks()
        surface.blit(self.image, (self.x - self.half_width, self.y - self.half_width))


