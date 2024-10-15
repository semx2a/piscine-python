import pytest
import numpy as np
from pimp_image import ft_blue
from load_image import ft_load


@pytest.mark.parametrize('path', [
    '../assets/animal.jpeg',
    '../assets/cat_ok.jpg',
    '../assets/giphy.webp',
    '../assets/image.png',
    '../assets/landscape.jpg'
])
def test_ft_blue_runs_without_errors(path):
    try:
        img = ft_load(path)
        ft_blue(img)
    except Exception as e:
        pytest.fail(f"ft_blue raised an exception: {e}")


@pytest.mark.parametrize('path', [
    '../assets/animal.jpeg',
    '../assets/cat_ok.jpg',
    '../assets/giphy.webp',
    '../assets/image.png',
    '../assets/landscape.jpg'
])
def test_ft_blue_output_dimensions(path):
    img = ft_load(path)
    blue_img = ft_blue(img)
    assert img.size == blue_img.size, \
        "Output image dimensions do not match input image dimensions"


@pytest.mark.parametrize('path', [
    '../assets/animal.jpeg',
    '../assets/cat_ok.jpg',
    '../assets/giphy.webp',
    '../assets/image.png',
    '../assets/landscape.jpg'
])
def test_ft_blue_output_type(path):
    img = ft_load(path)
    blue_img = ft_blue(img)
    assert isinstance(blue_img, np.ndarray), \
        "Output is not an instance of numpy.array"
