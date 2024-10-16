from load_image import ft_load
import pytest
import os


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
def test_ft_load_valid_image(path: str):
    image = ft_load(path)
    assert image is not None
    assert hasattr(image, 'shape')  # Example attribute check


@pytest.mark.parametrize('path', [
    os.path.join(current_dir, 'README.md'),
    os.path.join(current_dir, 'py02'),
    (''),
    (' '),
    ('            '),
    ('0'),
    ('111111111111111110'),
    os.path.join(assets_dir, 'cat_nok.jpg'),
    os.path.join(assets_dir, 'empty.jpg'),
    os.path.join(assets_dir, 'empty.jpeg'),
    os.path.join(assets_dir, 'empty.webp'),
    os.path.join(assets_dir, 'empty.png')
])
def test_ft_load_unsupported_format(path: str):
    with pytest.raises(SystemExit):
        ft_load(path)
