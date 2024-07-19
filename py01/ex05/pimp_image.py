import numpy as np
import cv2


def display_image(window_title: str, image: np.array) -> None:

    cv2.namedWindow(window_title, cv2.WINDOW_KEEPRATIO)
    cv2.imshow(window_title, image)

    wait_time = 1000
    while cv2.getWindowProperty(window_title, cv2.WND_PROP_VISIBLE) >= 1:
        keyCode = cv2.waitKey(wait_time)
        if (keyCode & 0xFF) == ord("q"):
            cv2.destroyAllWindows()
            break


def ft_invert(image: np.array) -> np.array:
    """ft_invert takes an array representation of an image to apply an
inversion filter"""
    try:
        negative_img = cv2.bitwise_not(image)
        display_image('Inverted filter', negative_img)

    except Exception as e: 
        print(f'Exception as {e}')

    return negative_img


def ft_red(image: np.array) -> np.array:
    """ft_red takes an array representation of an image to apply a
red filter"""

    try:
        # set blue and green chanels to 0
        red_img = image.copy()
        red_img[:, :, 0] = 0
        red_img[:, :, 1] = 0
        display_image('Red filter', red_img)

    except Exception as e:
        print(f'Exception: {e}')

    return red_img


def ft_green(image: np.array) -> np.array:
    """ft_green takes an array representation of an image to apply a
green filter"""
    try:
        # set blue and red chanels to 0
        green_img = image.copy()
        green_img[:, :, 0] = 0
        green_img[:, :, 2] = 0
        display_image('Green filter', green_img)

    except Exception as e:
        print(f'Exception: {e}')

    return green_img


def ft_blue(image: np.array) -> np.array:
    """ft_red takes an array representation of an image to apply a
blue filter"""
    try:
        # set green and red chanels to 0
        blue_img = image.copy()
        blue_img[:, :, 1] = 0
        blue_img[:, :, 2] = 0
        display_image('Blue filter', blue_img)

    except Exception as e:
        print(f'Exception: {e}')

    return blue_img


def ft_grey(image: np.array) -> np.array:
    """ft_grey takes an array representation of an image to apply a
red filter"""
    try:
        grey_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        display_image("Grey filter", grey_img)

    except Exception as e:
        print(f'Exception: {e}')

    return grey_img
