import numpy as np
import matplotlib.pyplot as plt

from load_image import ft_load


def rgb2gray(rgb: np.array) -> np.array:
    """
    Turns a RGB image to Grayscale

    Parameters:
    rgb (np.array): the 2D numpy array representation of the image.

    Return value:
    np.array: the 2D numpy array representation of the grayscale image.
    """
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.144])


def ft_zoom(img: np.array) -> np.array:
    """
    Zooms on an image.

    Parameters:
    img (np.array): the 2D numpy array representation an image.

    Return value:
    np.array: The zoomed image as a 2D numpy array
    """
    try:
        img_out = np.zeros_like(img)  # zero initialized table of img size

        h, w = img.shape  # unpacking image height and width
        zh, zw = 400, 400  # setting image final size
        eh = round((h - zh) // 2)
        ew = round((w - zw) // 2)  # computing margins

        # slicing numpy array to apply 'zoom'
        img_out = img[eh:eh + zh, ew:ew + zw]

        print(f"New shape after slicing: {img_out.shape}")
        print(img_out)

        return img_out

    except Exception as e:
        exit(f'Exception: {e}')


def transpose(array: np.array) -> np.array:
    """
    Transposes the given 2D numpy array.

    Parameters:
    array (np.array): A 2D numpy array to be transposed.

    Return value:
    np.array: A new 2D numpy array that is the transpose of the input array.
    """

    result = np.zeros((array.shape[1], array.shape[0]))

    # iterate through rows
    for i in range(array.shape[0]):
        # iterate through columns
        for j in range(array.shape[1]):
            result[j][i] = array[i][j]

    return result


def ft_rotate(path: str):
    """
    Rotates an image.

    Parameters:
    path (string): the path of the image to be rotated.

    Return value:
    None
    """
    try:
        img = ft_load(path)
        print(img)
        img = rgb2gray(img)  # converting image to greyscale
        zoomed_img = ft_zoom(img)
        rotated_img = transpose(zoomed_img)

        print(f"The shape after Transpose: {rotated_img.shape}")
        print(rotated_img)

        plt.imshow(rotated_img, cmap=plt.get_cmap('gray'))
        plt.show()

    except Exception as e:
        exit(f'Exception: {e}')
