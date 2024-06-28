from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    try:
        with Image.open(path) as image:
            image_array = np.array(image)
            return image_array
    except FileNotFoundError:
        print(f'File not found: {path}')
    except Image.UnidentifiedImageError:
        print(f'Invalid image file: {path}')
    except Exception as e:
        print(f'Exception: {e}')
    return None
