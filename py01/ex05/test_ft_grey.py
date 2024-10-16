import pytest
import os
import numpy as np
from pimp_image import ft_grey
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
def test_ft_grey_runs_without_errors(path):
    try:
        img = ft_load(path)
        ft_grey(img)
    except Exception as e:
        pytest.fail(f"ft_grey raised an exception: {e}")


@pytest.mark.parametrize('path', [
    os.path.join(assets_dir, 'animal.jpeg'),
    os.path.join(assets_dir, 'cat_ok.jpg'),
    os.path.join(assets_dir, 'image.png'),
    os.path.join(assets_dir, 'landscape.jpg'),
    os.path.join(assets_dir, 'giphy.webp')
])
def test_ft_grey_output_type(path):
    img = ft_load(path)
    grey_img = ft_grey(img)
    assert isinstance(grey_img, np.ndarray), \
        "Output is not an instance of numpy.array"


def test_ft_grey_output_dimensions():
    # Create a sample RGB image (3D array)
    image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

    # Apply the grey filter
    grey_image = ft_grey(image)

    # Check if the output dimensions are correct
    assert grey_image.shape == (100, 100), "Output dimensions are incorrect"


def test_ft_grey_output_values():
    # Create a sample RGB image (3D array)
    image = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                      [[255, 255, 0], [0, 255, 255], [255, 0, 255]],
                      [[255, 255, 255], [0, 0, 0], [127, 127, 127]]],
                     dtype=np.uint8)

    # Apply the grey filter
    grey_image = ft_grey(image)

    # Expected grey values using the formula: Y = 0.299*R + 0.587*G + 0.114*B
    expected_grey_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

    # Check if the output values are correct
    np.testing.assert_almost_equal(grey_image, expected_grey_image, decimal=1,
                                   err_msg="Output values are incorrect")


def test_ft_grey_invalid_input():
    # Create an invalid image (2D array)
    invalid_image = np.random.randint(0, 256, (100, 100), dtype=np.uint8)

    # Check if the function raises an exception for invalid input
    with pytest.raises(SystemExit):
        ft_grey(invalid_image)
