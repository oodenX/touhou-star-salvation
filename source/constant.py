import pygame
from pygame.draw import circle

fps = 60
s = 1000
# 游戏的大小， 然后游戏左边是640宽，右边是320宽
size = (960, 720)
caption = 'Touhou-Star-Salvation'

# 游戏的图标
icon = "./resources/icon/icon.png"

# 音乐
dialogue_bgm = "./resources/bgm/I've (I've sound) - 陽だまりの小部屋 [mqms2].mp3"
level_bgm = "./resources/bgm/金卡雷 - 风中花，雪中月.mp3"
failure_bgm = "./resources/bgm/man.mp3"
boss_bgm = "./resources/bgm/金卡雷 - 引燃夜空的星火.mp3"
success_bgm = "./resources/bgm/lightnessOnTheWay.mp3"
damage_sound = './resources/sound/se_tan01.wav'


# 字体
# font = pygame.font.SysFont(None, 48)
# 菜单的背景图
background = './resources/background/menu.png'
menu_hint = './resources/background/menu_hint.png'
menu_text = './resources/background/menu_text.png'

# 对话的背景图
dialogue_background = './resources/background/dialogue_background.png'

# 对话的图片
plot = './resources/plot/plot-'
plot_tip = './resources/plot/plot_tip.png'

# boss的背景图
boss_background = './resources/background/boss_background.png'
sanae1_image = './resources/enemy/sanae1.png'
sanae2_image = './resources/enemy/sanae2.png'
sanae3_image = './resources/enemy/sanae3.png'
magic_circle_image = './resources/enemy/magic_circle.png'
sanae_change_sound = './resources/sound/se_slash.wav'

# 关卡的左边和右边的背景图
level_background1 = './resources/background/level_background_left.png'
level_background2 = './resources/background/level_background_right.png'

# 右边的分数，生命，符卡logo,power
score_text = './resources/text/score_text.png'
life_text = './resources/text/life_text.png'
spell_text = './resources/text/spell_text.png'
power_text = './resources/text/power_text.png'
heart = './resources/text/heart.png'

# 玩家的图标
player_image = './resources/player/player_image.png'

# 敌人的图片
sprite_image = './resources/enemy/spirit.png'

# 自机的判定点
player_point = './resources/player/point.png'

# 弹幕
bullet_image = './resources/bullet/bact_bullet.png'
star_bullet_image = './resources/bullet/big_star_bullet.png'
glowing_bullet_image = './resources/bullet/glowing_bullet.png'
circle_bullet_image = './resources/bullet/circle_bullet.png'
big_bullet_red_image = './resources/bullet/big_bullet_red.png'
big_bullet_green_image = './resources/bullet/big_bullet_green.png'
big_bullet_blue_image = './resources/bullet/big_bullet_blue.png'
big_bullet_yellow_image = './resources/bullet/big_bullet_yellow.png'
small_star_bullet_image = './resources/bullet/small_star_bullet.png'
satsu_bullet_image = './resources/bullet/satsu_bullet.png'

# item的图片
item_image = './resources/item/item.png'

# 无敌时候的火焰
fire_image = './resources/player-fire/fire-'
failure_image = './resources/background/failure.png'
success_image = './resources/background/success.png'

# Boss背景
boss_background = './resources/background/boss_background.png'

speed = 1.0
