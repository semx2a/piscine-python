import pytest
import os
import numpy as np
from pimp_image import ft_green
from load_image import ft_load


# Determine the absolute path to the assets directory
current_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(current_dir, '../assets')


@pytest.mark.parametrize('path', [
    os.path.join(assets_dir, 'animal.jpeg'),
    os.path.join(assets_dir, 'cat_ok.jpg'),
    os.path.join(assets_dir, 'image.png'),
    os.path.join(assets_dir, 'landscape.jpg'),
    os.path.join(assets_dir, 'giphy.webp')
])
def test_ft_green_runs_without_errors(path):
    try:
        img = ft_load(path)
        ft_green(img)
    except Exception as e:
        pytest.fail(f"ft_green raised an exception: {e}")


@pytest.mark.parametrize('path', [
    os.path.join(assets_dir, 'animal.jpeg'),
    os.path.join(assets_dir, 'cat_ok.jpg'),
    os.path.join(assets_dir, 'image.png'),
    os.path.join(assets_dir, 'landscape.jpg'),
    os.path.join(assets_dir, 'giphy.webp')
])
def test_ft_green_output_dimensions(path):
    img = ft_load(path)
    green_img = ft_green(img)
    assert img.size == green_img.size, \
        "Output image dimensions do not match input image dimensions"


@pytest.mark.parametrize('path', [
    os.path.join(assets_dir, 'animal.jpeg'),
    os.path.join(assets_dir, 'cat_ok.jpg'),
    os.path.join(assets_dir, 'image.png'),
    os.path.join(assets_dir, 'landscape.jpg'),
    os.path.join(assets_dir, 'giphy.webp')
])
def test_ft_green_output_type(path):
    img = ft_load(path)
    green_img = ft_green(img)
    assert isinstance(green_img, np.ndarray), \
        "Output is not an instance of numpy.array"
