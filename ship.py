import pygame

class Ship:
    '''飞船类'''
    def __init__(self,ai_game):
        '''初始化飞船设置'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船图像，获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #把新飞船放在底部居中
        self.rect.midbottom = self.screen_rect.midbottom

        #在属性中存储小数
        self.x = float(self.rect.x)
        #飞船移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitem(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)