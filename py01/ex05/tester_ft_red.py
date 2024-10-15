import pytest
import numpy as np
from pimp_image import ft_red
from load_image import ft_load


@pytest.mark.parametrize('path', [
    '../assets/animal.jpeg',
    '../assets/cat_ok.jpg',
    '../assets/giphy.webp',
    '../assets/image.png',
    '../assets/landscape.jpg'
])
def test_ft_red_runs_without_errors(path):
    try:
        img = ft_load(path)
        ft_red(img)
    except Exception as e:
        pytest.fail(f"ft_red raised an exception: {e}")


@pytest.mark.parametrize('path', [
    '../assets/animal.jpeg',
    '../assets/cat_ok.jpg',
    '../assets/giphy.webp',
    '../assets/image.png',
    '../assets/landscape.jpg'
])
def test_ft_red_output_dimensions(path):
    img = ft_load(path)
    red_img = ft_red(img)
    assert img.size == red_img.size, \
        "Output image dimensions do not match input image dimensions"


@pytest.mark.parametrize('path', [
    '../assets/animal.jpeg',
    '../assets/cat_ok.jpg',
    '../assets/giphy.webp',
    '../assets/image.png',
    '../assets/landscape.jpg'
])
def test_ft_red_output_type(path):
    img = ft_load(path)
    red_img = ft_red(img)
    assert isinstance(red_img, np.ndarray), \
        "Output is not an instance of numpy.array"