import numpy as np
import matplotlib.pyplot as plt


def ft_invert(image: np.array) -> np.array:
    """ft_invert takes an array representation of an image to apply an
inversion filter"""
    pass
    try:
        # First condition requiered for PNG format
        if len(image.shape) == 3 and image.shape[2] == 4:
            r, g, b, a = np.split(image, 4, axis=2)
            rgb_image = np.concatenate((r, g, b), axis=2)
            negative_rgb = 255 - rgb_image
            # Reintegrate alpha channel to keep size identical to source file
            negative_img = np.concatenate((negative_rgb, a), axis=2)

        else:
            negative_img = 255 - image

        plt.imshow(negative_img)
        plt.title('Negative Image')
        plt.show()

    except Exception as e:
        exit(f'Exception as {e}')

    return negative_img


def ft_red(image: np.array) -> np.array:
    """ft_red takes an array representation of an image to apply a
red filter"""

    try:
        # set blue and green chanels to 0 (1 = G, 2 = B)
        red_img = image.copy()
        red_img[:, :, 1] = 0
        red_img[:, :, 2] = 0

        plt.imshow(red_img)
        plt.title('Red Image')
        plt.show()

    except Exception as e:
        exit(f'Exception: {e}')

    return red_img


def ft_green(image: np.array) -> np.array:
    """ft_green takes an array representation of an image to apply a
green filter"""
    try:
        # set blue and red chanels to 0 (0 = R, 2 = B)
        green_img = image.copy()
        green_img[:, :, 0] = 0
        green_img[:, :, 2] = 0

        plt.imshow(green_img)
        plt.title('Green Image')
        plt.show()

    except Exception as e:
        exit(f'Exception: {e}')

    return green_img


def ft_blue(image: np.array) -> np.array:
    """ft_red takes an array representation of an image to apply a
blue filter"""
    try:
        # set green and red chanels to 0 (0 = R; 1 = G)
        blue_img = image.copy()
        blue_img[:, :, 0] = 0
        blue_img[:, :, 1] = 0

        plt.imshow(blue_img)
        plt.title('Blue Image')
        plt.show()

    except Exception as e:
        exit(f'Exception: {e}')

    return blue_img


def ft_grey(image: np.array) -> np.array:
    """ft_grey takes an array representation of an image to apply a
red filter"""
    try:
        assert len(image.shape) >= 3, 'invalid input image'
        # Grayscale conversion formula: Y = 0.299*R + 0.587*G + 0.114*B
        grey_img = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

        plt.imshow(grey_img, cmap=plt.get_cmap('gray'))
        plt.title("Grey Image")
        plt.show()

    except Exception as e:
        exit(f'Exception: {e}')

    return grey_img
