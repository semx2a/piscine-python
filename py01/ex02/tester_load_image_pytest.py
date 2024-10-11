from PIL import Image
from load_image import ft_load
import pytest


def test_ft_load_valid_image():
    # Assuming ft_load takes a file path and returns an image object
    image = ft_load('../assets/animal.jpeg')
    assert image is not None
    assert hasattr(image, 'size')  # Example attribute check


def test_ft_load_nonexistent_image():
    with pytest.raises(FileNotFoundError):
        ft_load('path/to/nonexistent/image.jpg')


def test_ft_load_unsupported_format():
    with pytest.raises(Image.UnidentifiedImageError):  # Replace ValueError with the specific exception ft_load raises
        ft_load('./README.md')
