import sys,pygame

class AlienInvasion:
    '''管理游戏资源和行为'''

    def __init__(self) -> None:
        '''初始化游戏，创建游戏资源'''
        pygame.init()

        self.screen = pygame.display.set_mode((1280,720))
        pygame.display.set_caption('外星人入侵')

    def run_game(sefl):
        '''游戏主循环体'''
        while True:
            #监听鼠标和键盘事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #使绘制屏幕可见
            pygame.display.flip()

if __name__ == '__main__':
    #当当前文件执行，创建游戏实例并开始
    ai = AlienInvasion()
    ai.run_game()