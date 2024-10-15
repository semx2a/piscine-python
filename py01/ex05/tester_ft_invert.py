import pytest
from PIL import ImageChops
from PIL import Image
from pimp_image import ft_invert
from load_image import ft_load


@pytest.mark.parametrize('path', [
    '../assets/animal.jpeg',
    '../assets/cat_ok.jpg',
    '../assets/giphy.webp',
    '../assets/image.png',
    '../assets/landscape.jpg'
])
def test_ft_invert_runs_without_errors(path):
    try:
        img = ft_load(path)
        ft_invert(img)
    except Exception as e:
        pytest.fail(f"ft_invert raised an exception: {e}")


@pytest.mark.parametrize('path', [
    '../assets/animal.jpeg',
    '../assets/cat_ok.jpg',
    '../assets/giphy.webp',
    '../assets/image.png',
    '../assets/landscape.jpg'
])
def test_ft_invert_output_dimensions(path):
    img = ft_load(path)
    inverted_img = ft_invert(img)
    print(f'img size = {img.size} | inverted_img size = {inverted_img.size}')
    assert img.size == inverted_img.size, \
        "Output image dimensions do not match input image dimensions"


@pytest.mark.parametrize('path', [
    '../assets/animal.jpeg',
    '../assets/cat_ok.jpg',
    '../assets/giphy.webp',
    '../assets/image.png',
    '../assets/landscape.jpg'
])
def test_ft_invert_output_is_inverted(path):
    img = ft_load(path)

    inverted_img = ft_invert(img)
    double_inverted_img = ft_invert(inverted_img)

    pil_img = Image.fromarray(img)
    pil_double_inverted_img = Image.fromarray(double_inverted_img)

    diff = ImageChops.difference(pil_img, pil_double_inverted_img)
    assert not diff.getbbox(), \
        "Double inversion did not return the original image"
