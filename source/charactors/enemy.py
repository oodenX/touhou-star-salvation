import math
import pygame

# 敌人的父类
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y, size, images, hp, speed):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.speed = speed
        self.size = size
        self.timer = pygame.time.get_ticks()
        self.hp = hp
        self.timer1 = pygame.time.get_ticks()
        self.timer2 = pygame.time.get_ticks()
        self.dx, self.dy = self.calculate_direction()
        self.images = images
        self.moving_state_num = 0
        self.hit = False
        self.times1 = 0

    def calculate_direction(self):
        """
        计算敌人移动的方向（x, y分量）
        """
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        # 标准化向量，确保速度向量长度等于speed
        dx = dx * (self.speed / distance) if distance != 0 else 0
        dy = dy * (self.speed / distance) if distance != 0 else 0
        return dx, dy

    # 敌人运动的动画
    def time_waiting(self):
        if pygame.time.get_ticks() - self.timer2 > 50:
            self.timer2 = pygame.time.get_ticks()
            self.times1 += 1
        if self.times1 == 3:
            self.times1 = 0
            self.moving_state_num += 1
            if self.moving_state_num == len(self.images):
                self.moving_state_num = 0
    # 判断敌人是否死亡
    def is_dead(self):
        return self.hp <= 0 or self.out_of_screen()


    # 判断是否击中目标
    def is_hit(self, x, y):
        return (self.x - x) * (self.x - x) + (self.y - y) * (self.y - y) <= self.size * self.size

    # 判断是否被击中
    def check_hit(self, bullets):
        for bullet in bullets:
            if self.is_hit(bullet.center_x, bullet.center_y):
                self.hit = True
                self.hp -= 20
                bullets.remove(bullet)
            if self.is_dead():
                return

    # 判断是否出界
    def out_of_screen(self):
        return self.x < 0 or self.x > 640 or self.y < 0 or self.y > 720

    # 更新敌人的方法
    def update(self, surface, bullets):
        if pygame.time.get_ticks() - self.timer1 > 200:
            self.timer1 = pygame.time.get_ticks()
            self.x += self.dx
            self.y += self.dy
        self.time_waiting()
        self.check_hit(bullets)
        self.x += self.dx
        self.y += self.dy
        surface.blit(self.images[self.moving_state_num], (self.x - self.size, self.y - self.size))
