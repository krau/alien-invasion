import sys,pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.aliens = pygame.sprite.Group()

        self._creat_fleet()
        
    def run_game(self):
        '''游戏主循环体'''
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullets()
            self._update_alien()
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

    def _creat_fleet(self):
        '''创建外星人机群'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3*alien_height) - ship_height)
        number_rows = available_space_y // (2*alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._creat_alien(alien_number,row_number)

    def _creat_alien(self,alien_num,row_number):
        '''创建一个外星人并放在当前一行'''
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        alien.x = alien_width + 2*alien_width*alien_num
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_alien(self):
        '''更新外星人位置'''
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        '''外星人到达边缘时'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''向下移动外星人'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        #改变向下后的方向
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        #重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitem()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        #使绘制屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    #当前文件执行，创建游戏实例并开始
    ai = AlienInvasion()
    ai.run_game()