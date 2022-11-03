import pygame

class Ship:
    '''飞船类'''
    def __init__(self,ai_game):
        '''初始化飞船设置'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船图像，获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #把新飞船放在底部居中
        self.rect.midbottom = self.screen_rect.midbottom

    def blitem(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)