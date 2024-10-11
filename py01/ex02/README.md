# Exercise 02: load my image

## Description

| Program name | `load_image.py` |
| ------------ | --------------- |
| File to turn in | `load_image.py` |
| Allowed librairies | all libs for image loading and table manipulation |

## Instructions

Write a function that loads an image, prints its format, and its pixels content in RGB format.

JPG and JPEG formats compatibility is mandatory.
Any error should be caught and printed in the console with a clear error message.

Program prototype:

```python
def ft_load(path: str) -> array:
    pass
```

A tester is provided:

```python
from load_image import ft_load

print(ft_load("landscape.jpg"))
```

The output should be:

```bash
$> python tester.py
The shape of the image is: (257, 450, 3)
[[[19 42 83]
[23 42 84]
[28 43 84]
...
[0 0 0]
[1 1 1]
[1 1 1]]]
```

## References

- [Import Image Data into Numpy Arrays](https://www.pluralsight.com/resources/blog/guides/importing-image-data-into-numpy-arrays)
