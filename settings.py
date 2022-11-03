class Settings:
    '''存储设置'''
    def __init__(self):
        '''初始化游戏设置'''
        #屏幕设置
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230,230,230)
        
        #飞船设置
        self.ship_speed = 0.8

        #子弹设置
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_maxnums = 3