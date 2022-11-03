import sys,pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

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
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        '''游戏主循环体'''
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullets()
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
        '''响应按键按下'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire()

    def _check_keyup_events(self,event):
        '''响应按键松开'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire(self):
        '''创建子弹并加入编组'''
        if len(self.bullets) < self.settings.bullet_maxnums:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''更新子弹'''
        #更新位置
        self.bullets.update()

        #删除超出屏幕的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        #重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitem()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #使绘制屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    #当前文件执行，创建游戏实例并开始
    ai = AlienInvasion()
    ai.run_game()