import random

import pygame
from .enemy_summon import EnemySummon
from .. import constant as C
from ..charactors import myself
from ..items.score_point import ScorePoint
from ..items.power_point import PowerPoint
from ..charactors.butterfly_down import ButterflyDown1, ButterflyDown2, ButterflyDown3
from ..charactors.butterfly_left import ButterflyLeft1, ButterflyLeft2, ButterflyLeft3
from ..charactors.butterfly_right import ButterflyRight1, ButterflyRight2, ButterflyRight3
from ..bullets.bullet import Bullet
from ..bullets.star_bullet import StarBullet
from ..bullets.big_bullet_red import BigBulletRed
from ..bullets.big_bullet_green import BigBulletGreen
from ..bullets.big_bullet_blue import BigBulletBlue
from ..bullets.big_bullet_yellow import BigBulletYellow
from ..charactors.spirit1_down import Spirit1Down1, Spirit1Down2
from ..charactors.spirit1_left import Spirit1Left1, Spirit1Left2
from ..charactors.spirit1_right import Spirit1Right1, Spirit1Right2
from ..charactors.spirit2_down import Spirit2Down1, Spirit2Down2
from ..charactors.spirit2_left import Spirit2Left1, Spirit2Left2
from ..charactors.spirit2_right import Spirit2Right1, Spirit2Right2
from ..charactors.spirit3_down import Spirit3Down1, Spirit3Down2
from ..charactors.spirit3_left import Spirit3Left1, Spirit3Left2
from ..charactors.spirit3_right import Spirit3Right1, Spirit3Right2
from ..charactors.spirit4_down import Spirit4Down1, Spirit4Down2
from ..charactors.spirit4_left import Spirit4Left1, Spirit4Left2
from ..charactors.spirit4_right import Spirit4Right1, Spirit4Right2
from ..charactors.sanae import Sanae


class Boss:
    def __init__(self, Marisa, fire_state):
        self.screen = pygame.display.set_mode(C.size)
        self.background1 = pygame.image.load(C.boss_background)
        self.background2 = pygame.image.load(C.level_background2)
        self.life_text = pygame.image.load(C.life_text)
        self.spell_text = pygame.image.load(C.spell_text)
        self.score_text = pygame.image.load(C.score_text)
        self.power_text = pygame.image.load(C.power_text)
        self.heart_image = pygame.image.load(C.heart)
        self.Sanae = Sanae()
        self.Marisa = Marisa
        self.damage_sound = pygame.mixer.Sound(C.damage_sound)
        self.fire_state = fire_state
        self.i = 0
        self.timer1 = 0  # 控制移动动画
        self.timer2 = 0  # 控制火焰动画
        self.timer3 = 0  # 控制无敌时间
        self.timer4 = 0  # 控制得分点和火力点
        self.timer5 = 0
        self.moving_state_num = 0
        self.finished = False
        self.state1_bonus = False
        self.state2_bonus = False
        self.state3_bonus = False
        self.state4_bonus = False
        self.next = 'failure'   # 输了才是failure
        self.enemy_bullets = []
        self.score_points = []
        self.power_points = []
        self.enemys = []

    # 用来展示右边的信息
    def show_info(self, surface):
        font = pygame.font.SysFont('Arial', 36)
        score_text = font.render(str(self.Marisa.score), True, (0, 0, 0))
        power_text = font.render(f'{self.Marisa.power:.2f}', True, (0, 0, 0))
        surface.blit(self.score_text, (670, 24))
        surface.blit(score_text, (740, 14))
        surface.blit(self.power_text, (660, 200))
        surface.blit(power_text, (740, 200))

        surface.blit(self.life_text, (680, 64))
        max_lives = min(self.Marisa.life, 10)  # Ensure no more than 10 lives are displayed
        for i in range(max_lives):
            row = i // 5
            col = i % 5
            surface.blit(self.heart_image, (755 + col * 40, 54 + row * 40))  # Adjust position as needed

    # 用来展示背景
    def show_background(self, surface):
        surface.blit(self.background1, (0, 0))
        surface.blit(self.background2, (640, 0))

    # 用来计时的方法
    def time_waiting(self, timer, waiting):
        if pygame.time.get_ticks() - timer > waiting:
            return True
        return False

    # 用来更新移动动画的方法
    def moving_action(self):
        if (self.time_waiting(self.timer1, 180)):
            self.timer1 = pygame.time.get_ticks()
            self.moving_state_num += 1
            if self.moving_state_num == 8:
                self.moving_state_num = 0

    def sanae_bonus(self):
        if self.Sanae.state == 1 and self.state1_bonus == False:
            self.state1_bonus = True
            self.Marisa.score += int(10000 * self.Marisa.power)
            self.Marisa.power += 0.5
        if self.Sanae.state == 2 and self.state2_bonus == False:
            self.state2_bonus = True
            self.Marisa.score += int(10000 * self.Marisa.power)
            self.Marisa.power += 0.5
        if self.Sanae.state == 3 and self.state3_bonus == False:
            self.state3_bonus = True
            self.Marisa.score += int(10000 * self.Marisa.power)
            self.Marisa.power += 0.5
        if self.Sanae.state == 4 and self.state4_bonus == False:
            self.state4_bonus = True
            self.Marisa.score += int(10000 * self.Marisa.power)
            self.Marisa.power += 0.5

    # 用来展示火焰动画的方法
    def fire_show(self, surface):
        if self.Marisa.invincibility:
            if self.time_waiting(self.timer2, 150):
                self.timer2 = pygame.time.get_ticks()
                self.fire_state = random.randint(2, 10)
            image = pygame.image.load(C.fire_image + str(self.fire_state) + '.png')
            surface.blit(image, (self.Marisa.center_x - 6, self.Marisa.center_y + random.randint(-8, 5)))

    # 用来判断是否死亡的方法
    def check_alive(self):
        if self.Marisa.life == 0:
            self.next = 'failure'
            self.finished = True

    # 用来判断是否无敌的方法
    def is_invincibility(self):
        if self.Marisa.invincibility:
            if self.time_waiting(self.timer3, 3000):
                self.timer3 = pygame.time.get_ticks()
                self.Marisa.invincibility = False

    # 用来判断是否受伤的方法
    def is_hurt(self, x, y, para):
        if self.Marisa.invincibility:
            return
        if self.calculate(x, y, para):
            self.Marisa.invincibility = True
            self.timer3 = pygame.time.get_ticks()
            self.Marisa.life -= 1
            self.Marisa.power -= 0.5
            self.damage_sound.play()

    # 用来计算与Marisa之间的距离
    def calculate(self, x, y, para):
        return (self.Marisa.center_x - x) * (self.Marisa.center_x - x) + (self.Marisa.center_y - y) * (
                self.Marisa.center_y - y) <= para

    # 计算当前的得分和火力点
    def check_point(self, surface):
        for score_point in self.score_points:
            if score_point.state == 2:
                self.score_points.remove(score_point)
                self.Marisa.score += int(150 * self.Marisa.power)
            if score_point.state == 1:
                self.score_points.remove(score_point)
            if score_point.state == 0:
                score_point.update(surface, self.Marisa.center_x, self.Marisa.center_y)
        if self.Marisa.score >= 5000 * pow(2, self.i):
            self.Marisa.life += 1
            self.i += 1

        for power_point in self.power_points:
            if power_point.state == 2:
                self.power_points.remove(power_point)
                self.Marisa.power += 0.05
            if power_point.state == 1:
                self.power_points.remove(power_point)
            if power_point.state == 0:
                power_point.update(surface, self.Marisa.position_x, self.Marisa.position_y)

    # 展示和更新的方法
    def draw(self, surface, keys):
        self.show_background(surface)
        self.show_info(surface)
        player_image = self.Marisa.image.subsurface(self.Marisa.moving_animation(self.moving_state_num, keys))
        surface.blit(player_image, (self.Marisa.position_x, self.Marisa.position_y))
        if self.Marisa.rate == 0.5:
            surface.blit(self.Marisa.point, (self.Marisa.position_x - 16, self.Marisa.position_y - 8))

    # 获得得分和火力点的方法
    def bonus(self):
        # 每过两秒出现一个得分点和火力点:
        if self.time_waiting(self.timer4, 2 * C.s):
            self.timer4 = pygame.time.get_ticks()
            score_point = ScorePoint()
            power_point = PowerPoint()
            self.score_points.append(score_point)
            self.score_points.append(score_point)
            self.power_points.append(power_point)

    def update_enemys(self, surface):
        for enemy in self.enemys:
            enemy.shooting(surface, self.Marisa.bullets, self.enemy_bullets, self.Marisa.center_x, self.Marisa.center_y)
            if enemy.is_dead():
                self.enemys.remove(enemy)
                self.Marisa.score += int(100 * self.Marisa.power)
            self.is_hurt(enemy.x, enemy.y, enemy.size * enemy.size)

    def update_bullets(self, surface):
        for bullet in self.enemy_bullets:
            bullet.update(surface)
            self.is_invincibility()
            self.is_shot(bullet)
            if bullet.out_of_screen():
                self.enemy_bullets.remove(bullet)
    # 用来检查自己是否被击中的方法
    def is_shot(self, bullet):
        self.is_hurt(bullet.x, bullet.y, bullet.radius * bullet.radius)
        if self.calculate(bullet.x, bullet.y, bullet.radius * bullet.radius):
            self.enemy_bullets.remove(bullet)

    # 用来是否打败boss
    def success(self):
        if self.Sanae.alive == False:
            self.next = 'success'
            self.finished = True

    # 用来更新的方法
    def update(self, surface, keys):
        self.draw(surface, keys)
        self.Marisa.update(surface, keys)
        self.check_point(surface)
        self.check_alive()
        self.is_hurt(self.Sanae.x, self.Sanae.y, self.Sanae.size * self.Sanae.size)
        self.moving_action()
        self.fire_show(surface)
        self.is_invincibility()
        self.bonus()
        self.sanae_bonus()
        self.Sanae.update(surface, self.Marisa.bullets, self.Marisa, self.enemy_bullets)
        self.update_bullets(surface)
        self.success()
