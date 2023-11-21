import time
import pyautogui
from PIL import Image, ImageDraw
import tkinter as tk

MARGIN = 30

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
    #draw.rectangle([(mouse_x-MARGIN, mouse_y-MARGIN), (mouse_x+MARGIN, mouse_y+MARGIN)], fill=(255, 0, 0, 128))  # Red rectangle with alpha
    root = tk.Tk()
    root.overrideredirect(True)
    root.geometry("+0+0")
    root.lift()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.wm_attributes("-transparentcolor", "white")

    canvas = tk.Canvas(root, bg='white', width=2560, height=1440)
    
    canvas.create_rectangle(mouse_x-MARGIN, mouse_y-MARGIN, mouse_x+MARGIN, mouse_y+MARGIN, outline='black', fill='blue')
    canvas["state"] = "disabled"
    canvas.pack()
        
    
    
    #root.mainloop()

def main():
    mouse_x, mouse_y = get_mouse_position()
    
    image = get_screen_image()
    
    dim_and_highlight(mouse_x, mouse_y, image)

if __name__ == "__main__":
    
    main()