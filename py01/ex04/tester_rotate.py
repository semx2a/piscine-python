import pytest

from rotate import ft_rotate


@pytest.mark.parametrize('path', [
    "../assets/animal.jpeg",
    "../assets/cat_ok.jpg",
    "../assets/image.png",
    "../assets/landscape.jpg",
    "../assets/giphy.webp"
])
def test_ft_zoom_valid_image(path: str):
    ft_rotate(path)


@pytest.mark.parametrize('path', [
    "../assets/cat_nok.jpg",
    './README.md',
    '../py02',
    '',
    ' ',
    '            ',
    '0',
    '111111111111111110',
    '../assets/empty.jpg',
    '../assets/empty.jpeg',
    '../assets/empty.webp',
    '../assets/empty.png'
])
def test_ft_zoom_unsupported_format(path: str):
    with pytest.raises(SystemExit):
        ft_rotate(path)
