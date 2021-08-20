
class Settings():
    
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = 230, 230, 230
        
        # Button settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # Ship limit
        self.ship_limit = 3

        # Speeding up
        self.speed_up = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 2
        self.ship_speed_factor = 1.5
    
    def increase_speed(self):
        self.alien_speed_factor *= self.speed_up
        self.bullet_speed_factor *= self.speed_up
        self.ship_speed_factor *= self.speed_up