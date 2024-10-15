# Exercise 03: Zoom on Me

## Description

| Program name | `zoom.py` |
| ------------ | --------- |
|File to turn in | `load_image.py` `zoom.py` |
| Allowed functions | all libs for loading, manipulating, displaying image and table manipulation |

## Instructions

Create a program that loads the image "animal.jpeg", prints its information and displays it after applying a zoom.

- Display the size in pixels on the X and Y axis.
- Display the number of channels.
- Display the pixel content of the image.
- Display scales on the x and y axis of the image.

The program must not stop abruptly and should handle erros with clear messages.

Expected output:

```bash
$> python zoom.py
The shape of image is: (768, 1024, 3)
[[[120 111 132]
[139 130 151]
[155 146 167]
...
[120 156 94]
[119 154 90]
[118 153 89]]]
New shape after slicing: (400, 400, 1) or (400, 400)
[[[167]
[180]
[194]
...
[102]
[104]
[103]]]
$>
```

## References

- [Convert RGB to Grayscale](https://www.askpython.com/python-modules/matplotlib/convert-rgb-to-grayscale)
- [Catching KeyboardInterrupt in Python](https://stackoverflow.com/questions/21120947/catching-keyboardinterrupt-in-python-during-program-shutdown)