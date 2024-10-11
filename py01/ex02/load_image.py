from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    try:
        with Image.open(path) as image:
            image_array = np.array(image)
            print(f'The shape of the image is: {image_array.shape}')
            return image_array
    except FileNotFoundError:
        print(f'File not found: {path}')
        raise
    except ValueError:
        print(f'Unsupported format: {path}')
        raise
    except Image.UnidentifiedImageError:
        print(f'Invalid image file: {path}')
        raise
    except Exception as e:
        print(f'Exception: {e}')
        raise
    return None
