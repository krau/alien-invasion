class Gamestats:
    '''统计游戏信息'''

    def __init__(self,ai_game) -> None:
        '''初始化统计信息'''
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit