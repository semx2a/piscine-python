import cv2
import numpy as np


def ft_load(path: str) -> np.array:
    try:
        image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        image_array = np.array(image)
        print(f'The shape of the image is: {image_array.shape}')
        return image_array
    except FileNotFoundError:
        print(f'File not found: {path}')
    except cv2.error():
        print(f'Invalid image file: {path}')
    except Exception as e:
        print(f'Exception: {e}')
    return None
