import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the window size and title
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Define colors and font
background_color = (255, 255, 255)
menu_color = (200, 200, 200)
cell_color = (100, 100, 100)
font = pygame.font.Font(None, 30)
user_text_direction = ''
user_text_value = ''
input_rect1 = pygame.Rect(630, 340, 140, 32)
input_rect2 = pygame.Rect(630, 380, 140, 32)
# color_passive store color which is
# color of input box.
color_passive = pygame.Color('white')
color = color_passive
# Define the menu function
def draw_menu():
    # Draw the menu background
    menu_rect = pygame.Rect(600, 0, 200, 600)
    pygame.draw.rect(screen, menu_color, menu_rect)

    # Draw the cells in the upper part of the menu
    cell_rects = []
    for i in range(3):
        cell_rect = pygame.Rect(620, 50 + i*100, 160, 80)
        pygame.draw.rect(screen, cell_color, cell_rect)
        cell_text = font.render("Cell {}".format(i+1), True, (255, 255, 255))
        screen.blit(cell_text, (640, 70 + i*100))
        cell_rects.append(cell_rect)

    # Draw the settings in the lower part of the menu
    direction_text = font.render("Direction: ", True, (0, 0, 0))
    screen.blit(direction_text, (620, 340))
    amount_text = font.render("Value: ", True, (0, 0, 0))
    screen.blit(amount_text, (620, 380))

    pygame.display.update()

# Define the event handling function
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for cell_rect in cell_rects:
                if cell_rect.collidepoint(mouse_pos):
                    print("Cell clicked!")
            if input_rect1.collidepoint(event.pos):
                if event.type == pygame.KEYDOWN:
                    user_text_direction += event.unicode
            elif input_rect2.collidepoint(event.pos):
                if event.type == pygame.KEYDOWN:
                    user_text_value += event.unicode

# Main loop
while True:
    # Clear the screen and draw the menu
    screen.fill(background_color)
    draw_menu()
    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
      
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width()+10)
      
    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()
    # Handle events
    handle_events()
    

    # Update the screen
    pygame.display.update()

    # Set the frame rate
    pygame.time.Clock().tick(60)
   
