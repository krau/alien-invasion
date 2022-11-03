import sys,pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    '''管理游戏资源和行为'''

    def __init__(self):
        '''初始化游戏，创建游戏资源'''
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width , self.settings.screen_height))
        pygame.display.set_caption('外星人入侵')

        self.ship = Ship(self)
        
    def run_game(self):
        '''游戏主循环体'''
        while True:
            self._check_event()
            self.ship.update()
            self._update_screen()

    def _check_event(self):
        #监听鼠标和键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self,event):
        '''相应按键按下'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        '''相应按键松开'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        #重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitem()
        #使绘制屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    #当前文件执行，创建游戏实例并开始
    ai = AlienInvasion()
    ai.run_game()