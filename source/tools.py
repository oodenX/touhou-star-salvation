import pygame
import os
import source.constant as C
from source.state.boss import Boss

class Game:
    def __init__(self, state_dict, start_state):
        self.surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        # 获得初始状态
        self.state_dict = state_dict
        self.state = self.state_dict[start_state]
        self.score_points = []
        self.power_points = []


    def update(self):
        # 每次一个状态结束后就去这个状态的下一个状态
        if self.state.finished:
            next_state = self.state.next
            self.state.finished = False
            if next_state == 'boss':
                self.state = Boss(self.state.Marisa, self.state.fire_state)
            else:
                self.state = self.state_dict[next_state]
            # 根据不同的状态，播放不同的BGM
            if next_state == 'dialogue':
                music_file = C.dialogue_bgm
                pygame.mixer.music.load(music_file)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.5)
            elif next_state == 'level':
                pygame.mixer.music.stop()
                music_file = C.level_bgm
                pygame.mixer.music.load(music_file)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.2)
            elif next_state == 'failure':
                pygame.mixer.music.stop()
                music_file = C.failure_bgm
                pygame.mixer.music.load(music_file)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.3)
            elif next_state == 'boss':
                pygame.mixer.music.stop()
                music_file = C.boss_bgm
                pygame.mixer.music.load(music_file)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.3)
            elif next_state == 'success':
                pygame.mixer.music.stop()
                music_file = C.success_bgm
                pygame.mixer.music.load(music_file)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.5)
            elif next_state == 'exit':
                pygame.mixer.music.stop()
                pygame.quit()
        # 注意这个state是一个类
        self.state.update(self.surface, self.keys)

    def run(self):
        # 加载游戏名，图标
        pygame.display.set_caption(C.caption)
        icon = pygame.image.load(C.icon)
        pygame.display.set_icon(icon)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            self.update()
            pygame.display.update()
            # 游戏的fps最多60
            self.clock.tick(C.fps)