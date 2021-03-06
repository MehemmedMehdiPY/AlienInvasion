import pygame.font

class Button():
    def __init__(self, screen, ai_settings, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
     
        self.text_color = 255, 255, 255
        self.button_color = 0, 255, 0

        self.rect = pygame.Rect(0, 0, ai_settings.button_width, 
                            ai_settings.button_height)
        
        # Set font as Default by entering None
        # Set the size of text
        self.font = pygame.font.SysFont(None, 48)
        self.rect.center = self.screen_rect.center
   
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, 
                            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()

        self.msg_image_rect.center = self.screen_rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)