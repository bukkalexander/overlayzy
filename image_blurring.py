import cv2
import numpy as np
import pathlib

PROJECT_PATH = pathlib.Path(__file__).parent.resolve()
PRESENTATION_SLIDE_IMAGE_FILE_PATH = PROJECT_PATH / "temppic.png"
PROCESSED_PRESENTATION_SLIDE_IMAGE_FILE_PATH = PROJECT_PATH / "temppic_processed.png"

class Detection:
    def __init__(self, left, top, right, bottom, name=""):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.name = name

    @property
    def width(self): 
        return self.right-self.left

    @property
    def height(self): 
        return self.bottom-self.top

    def row_range(self):
        return range(self.top, self.bottom)

    def col_range(self):
        return range(self.left, self.right)

class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x


def get_image(image_file_path):
    return cv2.imread(str(image_file_path))


def get_detection_list(image):
    detection_list = []

    detection_list.append(Detection(20,435,1040,490,"bullet 1"))
    detection_list.append(Detection(20,520,1350,585,"bullet 2"))
    detection_list.append(Detection(20,620,1380,760,"bullet 3"))
    detection_list.append(Detection(20,790,870,840,"bullet 4"))
    detection_list.append(Detection(1190,40,1860,360,"picture"))
    return detection_list


def select_detection(detection_list, mouse_point):
    for detection in detection_list:
        is_x_inside=mouse_point.x >= detection.left and mouse_point.x <= detection.right
        is_y_inside=mouse_point.y >= detection.top and mouse_point.y <= detection.bottom
        if is_x_inside and is_y_inside: 
            return detection

    return None

def get_image_mask(image, detection):
    image_mask = np.zeros((image.shape[0], image.shape[1]), dtype=bool)
    for row in detection.row_range():
        for col in detection.col_range():
            image_mask[row, col] = True
    return image_mask


def get_masked_image(image, image_mask):
    kernel_size=(53,53)
    # Apply Gaussian blur
    masked_image = cv2.GaussianBlur(image, kernel_size, 0)
    masked_image[image_mask] = image[image_mask]
    return masked_image

def save_image(image_file_path, image):
    cv2.imwrite(str(image_file_path), image)
    print(f"saved image: {image_file_path}")


def get_detection(mouse_point):
    # 1. Define image size and read image to numpy array
    image_file_path = PRESENTATION_SLIDE_IMAGE_FILE_PATH
    image = get_image(image_file_path)

    # 2. Hard code object that contains rectangle of detected object in image
    detection_list = get_detection_list(image)


    detection = select_detection(detection_list, mouse_point)
    # if not detection is None:
    #     print(detection.name)

    #     # 3. fill image mask with value True for each (row, col) that is inside the selected object
    #     image_mask = get_image_mask(image, detection)
        
    #     # 4. Modify original image for image mask indices 
    #     processed_image = get_masked_image(image, image_mask)
        
    #     # 5. save the new image to file
    #     processed_image_file_path = PROCESSED_PRESENTATION_SLIDE_IMAGE_FILE_PATH
    #     save_image(processed_image_file_path, processed_image)

    return detection

if __name__=='__main__':
        
    mouse_point = Point(x=21, y=621)

    get_detection(mouse_point)