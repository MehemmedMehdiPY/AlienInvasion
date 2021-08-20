import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.button_width, self.button_height = 200, 50
        self.text_color = 255, 255, 255
        self.button_color = 0, 255, 0


        # Default font and size of text
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, 
                self.button_width, self.button_height)
        self.rect.center = self.screen_rect.center
        
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, 
                    self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        # We center the msg image into the position of button 
        self.msg_image_rect.center = self.screen_rect.center

    def draw_button(self):
        # Draw blank button and then draw messages
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
