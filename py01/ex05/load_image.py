from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    try:
        image = Image.open(path)
        image_array = np.array(image)
        print(f'The shape of the image is: {image_array.shape}')
        return image_array
    except FileNotFoundError:
        print(f'File not found: {path}')
    except Exception as e:
        print(f'Exception: {e}')
    return None
