import pytest
import numpy as np
from pimp_image import ft_green
from load_image import ft_load


@pytest.mark.parametrize('path', [
    '../assets/animal.jpeg',
    '../assets/cat_ok.jpg',
    '../assets/giphy.webp',
    '../assets/image.png',
    '../assets/landscape.jpg'
])
def test_ft_green_runs_without_errors(path):
    try:
        img = ft_load(path)
        ft_green(img)
    except Exception as e:
        pytest.fail(f"ft_green raised an exception: {e}")


@pytest.mark.parametrize('path', [
    '../assets/animal.jpeg',
    '../assets/cat_ok.jpg',
    '../assets/giphy.webp',
    '../assets/image.png',
    '../assets/landscape.jpg'
])
def test_ft_green_output_dimensions(path):
    img = ft_load(path)
    green_img = ft_green(img)
    assert img.size == green_img.size, \
        "Output image dimensions do not match input image dimensions"


@pytest.mark.parametrize('path', [
    '../assets/animal.jpeg',
    '../assets/cat_ok.jpg',
    '../assets/giphy.webp',
    '../assets/image.png',
    '../assets/landscape.jpg'
])
def test_ft_green_output_type(path):
    img = ft_load(path)
    green_img = ft_green(img)
    assert isinstance(green_img, np.ndarray), \
        "Output is not an instance of numpy.array"