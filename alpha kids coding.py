import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)


WHITE = (255, 255, 255)
RED = (255, 0, 0)


background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, WINDOW_SIZE)


age_icon = pygame.image.load("input age.png")

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Alpha Kids")

# Define Button class
class Button:
    def _init_(self, image_path, position):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=position)
        def draw(self):
        screen.blit(self.image, self.rect)

# Function to handle mouse click event
def handle_click(button, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button.rect.collidepoint(event.pos):
            if button == start_button:
                
                age_input_page()
            elif button == setting_button:
             
                settings_page()
            elif button == exit_button:
                       
                pygame.quit()
                sys.exit()

def age_input_page():
    age_input = ""
    font = pygame.font.Font(None, 36)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Age input:", age_input)
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    age_input = age_input[:-1]
                else:
                    age_input += event.unicode
        

        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))


        screen.blit(age_icon, (WIDTH // 2 - age_icon.get_width() // 2, HEIGHT // 3))
        input_text = font.render(age_input, True, RED)
        screen.blit(input_text, (WIDTH // 2 - input_text.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()

        if not running:
            level_selection_page()


def level_selection_page():
    level_icons = ["level 1.png", "level 2.png", "level 3.png"]
    y_position = HEIGHT // 4  
    level_buttons = []
    for icon in level_icons:
        level_button = Button(icon, (WIDTH // 2, y_position))
        level_buttons.append(level_button)
        y_position += 150  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 


        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))
        for button in level_buttons:
            button.draw()
        pygame.display.flip()
        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))
        for button in level_buttons:
            button.draw()
        pygame.display.flip()

def settings_page():
    running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  
                    return  
     
        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))

        font = pygame.font.SysFont(None, 36)
        text = font.render("Sound Options:", True, RED)  # Red color
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 3))

  
        sound_on_button = Button("sound on.png", (WIDTH // 2, HEIGHT // 2))
        sound_off_button = Button("sound off.png", (WIDTH // 2, 2 * HEIGHT // 3))
        save_button = Button("save game.png", (WIDTH // 2, 3 * HEIGHT // 4))
        load_button = Button("load game.png", (WIDTH // 2, 7 * HEIGHT // 8))

        sound_on_button.draw()
        sound_off_button.draw()
        save_button.draw()
        load_button.draw()

      
        pygame.display.flip()

start_button = Button("Start.png", (WIDTH // 2, HEIGHT // 3))
setting_button = Button("setting.png", (WIDTH // 2, HEIGHT // 2))
exit_button = Button("exit.png", (WIDTH // 2, 2 * HEIGHT // 3))

# Main game loop
running = True
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            handle_click(start_button, event)
        handle_click(setting_button, event)
        handle_click(exit_button, event)  

    screen.fill(WHITE)

    screen.blit(background_image, (0, 0))

    start_button.draw()
    setting_button.draw()
    exit_button.draw()

    pygame.display.flip()


pygame.quit()
sys.exit()





