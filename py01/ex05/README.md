# Exercise 05: Pimp my Image

## Description

| Program name | `pimp_image.py` |
| ------------ | --------------- |
| File to turn in | `load_image.py` `pimp_image.py` |
| Allowed functions | all libs for loading, manipulating, displaying image and table manipulation |

## Instructions

You need to develop five functions capable of applying a variety of color filters to images, while keeping the image the same.

Here's how they should be prototyped:

```python
def ft_invert(array) -> array:
    pass

def ft_red(array) -> array:
    pass

def ft_green(array) -> array:
    pass

def ft_blue(array) -> array:
    pass

def ft_grey(array) -> array:
    pass
```

Here's some restriction operators for each function: (you can only use those given, you don't have to use them all)

- invert: `=` `+` `-` `*`
- red: `=` `*`
- green: `=` `-`
- blue: `=`
- grey: `=` `/`

Here's a tester:

```python
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

array = ft_load("landscape.jpg")

ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)

print(ft_invert.__doc__)
print(ft_red.__doc__)
print(ft_green.__doc__)
print(ft_blue.__doc__)
print(ft_grey.__doc__)
```

Expected output:

```bash
$> python tester.py
The shape of the image is: (257, 450, 3)
[[[19 42 83]
[23 42 84]
[28 43 84]
...
[ 0 0 0]
[ 1 1 1]
[ 1 1 1]]]
...
Inverts the colors of the image received.
```

## References

- [A demonstration of filters in image processessing](https://abboahbaah.medium.com/a-demonstration-of-filters-in-image-processing-b180a00584e6)
- [Understanding image filters with Pyton] (https://deepnote.com/app/gabriele-tazzari-4ac1/Understanding-image-filters-with-Python-d6d7ff84-29f0-4466-a6f0-c5c3dc05345f)
- [ How to do image processing in Python](https://dataheadhunters.com/academy/how-to-do-image-processing-in-python-step-by-step-guide/)
- [OpenCV: Detect whether a window is close. Or close by press 'x' button](https://medium.com/@mh_yip/opencv-detect-whether-a-window-is-closed-or-close-by-press-x-button-ee51616f7088)
 
