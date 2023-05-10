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
input_rect1 = pygame.Rect(630, 360, 140, 32)
input_rect2 = pygame.Rect(630, 450, 140, 32)
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
    global cell_rects
    cell_rects = []
    for i in range(3):
        cell_rect = pygame.Rect(620, 50 + i * 100, 160, 80)
        pygame.draw.rect(screen, cell_color, cell_rect)
        cell_text = font.render("Cell {}".format(i + 1), True, (255, 255, 255))
        screen.blit(cell_text, (640, 70 + i * 100))
        cell_rects.append(cell_rect)

    # Draw the settings in the lower part of the menu
    direction_text = font.render("Direction: ", True, (0, 0, 0))
    screen.blit(direction_text, (620, 340))
    amount_text = font.render("Value: ", True, (0, 0, 0))
    screen.blit(amount_text, (620, 430))

    pygame.display.update()


active = 0
# Define the event handling function
def handle_events():
    global user_text_direction
    global user_text_value
    global active
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
                active = 1
            elif input_rect2.collidepoint(event.pos):
                active = 2
            else:
                active = 0
        if event.type == pygame.KEYDOWN:
            if active == 1:
                if event.key == pygame.K_RETURN:
                    user_text_direction = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text_direction = user_text_direction[:-1]
                elif event.key == pygame.K_RIGHT:
                    user_text_direction = ''
                    user_text_direction += 'Right'
                elif event.key == pygame.K_LEFT:
                    user_text_direction = ''
                    user_text_direction += 'Left'
                elif event.key == pygame.K_UP:
                    user_text_direction = ''
                    user_text_direction += 'Up'
                elif event.key == pygame.K_DOWN:
                    user_text_direction = ''
                    user_text_direction += 'Down'
                else:
                    print('error')
            elif active == 2:
                if event.key == pygame.K_RETURN:
                    user_text_value = ''
                elif event.key == pygame.K_BACKSPACE:
                            user_text_value = user_text_value[:-1]
                else:
                    user_text_value += event.unicode
                    if user_text_value.isdigit() == False:
                        print('error')


# Main loop
while True:
    handle_events()
    # Clear the screen
    screen.fill(background_color)
    draw_menu()
    # Handle events
    pygame.draw.rect(screen, color, input_rect1)
    text_surface1 = font.render(user_text_direction, True, (0, 0, 0))
    pygame.draw.rect(screen, color, input_rect2)
    text_surface2 = font.render(user_text_value, True, (0, 0, 0))
    # render at position stated in arguments
    screen.blit(text_surface1, (input_rect1.x, input_rect1.y + 20))
    screen.blit(text_surface2, (input_rect2.x, input_rect2.y + 20))
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect1.w = max(100, text_surface1.get_width() + 10)
    input_rect2.w = max(100, text_surface2.get_width() + 10)
    # display.flip() will update only a portion of the
    # screen to updated, not full area

    pygame.display.flip()


    # Update the screen
    pygame.display.update()

    # Set the frame rate
    pygame.time.Clock().tick(60)
