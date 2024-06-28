import sys
import os
from load_image import ft_load
import numpy as np
from matplotlib import pyplot


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.144])


def transpose(array: np.array) -> np.array:

    result = np.zeros(array.shape)

    # iterate through rows
    for i in range(len(array)):
        # iterate through colums
        for j in range(len(array[0])):
            result[j][i] = array[i][j]

    return result


def ft_rotate(path: str):
    try:
        racoon_img = ft_load(path)
        racoon_img = rgb2gray(racoon_img)  # converting image to grescale
        racoon_img = racoon_img[100:500, 450:850]  # slicing image to zoom

        print(f"The shape of the image is: {racoon_img.shape}")
        print(racoon_img)

        racoon_img = transpose(racoon_img)
        print(f"The shape after Transpose: {racoon_img.shape}")
        print(racoon_img)

        pyplot.imshow(racoon_img, cmap=pyplot.get_cmap('gray'))
        pyplot.show()

    except Exception as e:
        print(f'Exception: {e}')


def main():
    try:
        ft_rotate("../assets/animal.jpeg")
    except Exception as e:
        print(f"Excpetion: {e}")
        return 1
    return 0


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
