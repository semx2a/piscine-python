from load_image import ft_load
import pytest


@pytest.mark.parametrize('path', [
    ("../assets/animal.jpeg"),
    ("../assets/cat_ok.jpg"),
    ("../assets/image.png"),
    ("../assets/landscape.jpg"),
    ("../assets/giphy.webp")
    ])
def test_ft_load_valid_image(path: str):
    image = ft_load(path)
    assert image is not None
    assert hasattr(image, 'shape')  # Example attribute check


@pytest.mark.parametrize('path', [
    ("../assets/cat_nok.jpg"),
    ('./README.md'),
    ('../py02'),
    (''),
    (' '),
    ('            '),
    ('0'),
    ('111111111111111110'),
    ('../assets/empty.jpg'),
    ('../assets/empty.jpeg'),
    ('../assets/empty.webp'),
    ('../assets/empty.png')
])
def test_ft_load_unsupported_format(path: str):
    with pytest.raises(SystemExit):
        ft_load(path)
