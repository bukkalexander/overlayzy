import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 500, 500
flags = pygame.NOFRAME
window = pygame.display.set_mode((width, height), flags)
pygame.display.set_caption("Transparent Window")
pygame.mouse.set_visible(False)

# Make the window clickthrough
pygame.event.set_grab(True)

# Set the window transparency
window.set_alpha(None)

# Define colors
BLACK = (255, 0, 128)  # Transparent black

# # Create layered window
# hwnd = pygame.display.get_wm_info()["window"]
# win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
#                        win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# # Set window transparency color
# win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Clear the window
    window.fill(BLACK)

    # Draw your objects centered around the mouse position
    pygame.draw.rect(window, (255, 255, 255), (mouse_x - 25, mouse_y - 25, 50, 50))

    # Update the window
    pygame.display.flip()