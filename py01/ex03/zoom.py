import numpy as np
import matplotlib.pyplot as plt

from load_image import ft_load


def rgb2gray(rgb) -> np.array:
    """
    Turns a RGB image to Grayscale

    Parameters:
    rgb (np.array): the 2D numpy array representation of the image.

    Return value:
    np.array: the 2D numpy array representation of the grayscale image.
    """
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1440])


def ft_zoom(path: str):
    """
    Zooms on an image.

    Parameters:
    path (string): the path of the image to be rotated.

    Return value:
    np.array: The zoomed image as a 2D numpy array
    """
    try:
        img = ft_load(path)
        print(img)

        img = rgb2gray(img)  # converting image to grescale

        h, w = img.shape  # unpacking image height and width
        zh, zw = 400, 400  # setting image final size
        eh = round((h - zh) // 2)
        ew = round((w - zw) // 2)  # computing margins

        # slicing numpy array to apply 'zoom'
        img_out = img[eh:eh + zh, ew:ew + zw]

        print(f"New shape after slicing: {img_out.shape}")
        print(img_out)

        plt.imshow(img_out, cmap=plt.get_cmap('gray'))
        plt.show()

    except Exception as e:
        exit(f'Exception: {e}')
