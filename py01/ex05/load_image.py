from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Loads an image and returns it as a numpy array

    Parameters:
    path (string): the path of the image to be rotated.

    Return value:
    np.array: the 2D numpy array representation of the image.
    """
    try:
        with Image.open(path) as image:
            image_array = np.array(image)
            print(f'The shape of the image is: {image_array.shape}')
            return image_array

    except Exception as e:
        exit(f'Exception: {e}')
    return None
