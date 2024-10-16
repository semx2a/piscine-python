import pytest
import os
import numpy as np
from pimp_image import ft_blue
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
def test_ft_blue_runs_without_errors(path):
    try:
        img = ft_load(path)
        ft_blue(img)
    except Exception as e:
        pytest.fail(f"ft_blue raised an exception: {e}")


@pytest.mark.parametrize('path', [
    os.path.join(assets_dir, 'animal.jpeg'),
    os.path.join(assets_dir, 'cat_ok.jpg'),
    os.path.join(assets_dir, 'image.png'),
    os.path.join(assets_dir, 'landscape.jpg'),
    os.path.join(assets_dir, 'giphy.webp')
])
def test_ft_blue_output_dimensions(path):
    img = ft_load(path)
    blue_img = ft_blue(img)
    assert img.size == blue_img.size, \
        "Output image dimensions do not match input image dimensions"


@pytest.mark.parametrize('path', [
    os.path.join(assets_dir, 'animal.jpeg'),
    os.path.join(assets_dir, 'cat_ok.jpg'),
    os.path.join(assets_dir, 'image.png'),
    os.path.join(assets_dir, 'landscape.jpg'),
    os.path.join(assets_dir, 'giphy.webp')
])
def test_ft_blue_output_type(path):
    img = ft_load(path)
    blue_img = ft_blue(img)
    assert isinstance(blue_img, np.ndarray), \
        "Output is not an instance of numpy.array"
