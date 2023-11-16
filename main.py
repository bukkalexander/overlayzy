import time
import pyautogui
from PIL import Image, ImageDraw

MARGIN = 200

def get_mouse_position():
    # Get the mouse position
    mouse_x, mouse_y = pyautogui.position()

    # Print the coordinates
    print(f"Mouse position: x={mouse_x}, y={mouse_y}")
    return mouse_x, mouse_y

def get_screen_image():
    # Take a screenshot of the entire screen
    screenshot = pyautogui.screenshot()
    return screenshot


def dim_and_highlight(mouse_x, mouse_y, image):
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    draw.rectangle([(mouse_x-MARGIN, mouse_y-MARGIN), (mouse_x+MARGIN, mouse_y+MARGIN)], fill=(255, 0, 0, 128))  # Red rectangle with alpha
    screenshot = Image.alpha_composite(image.convert("RGBA"), overlay)
    screenshot.show()

def main():
    mouse_x, mouse_y = get_mouse_position()
    
    image = get_screen_image()
    
    dim_and_highlight(mouse_x, mouse_y, image)

if __name__ == "__main__":
    main()