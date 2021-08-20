
class GameStats():
    def __init__(self, cb_settings):
        self.cb_settings = cb_settings

        self.missed_target = cb_settings.missed_targets
        self.game_active = True
        