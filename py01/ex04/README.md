# Exercise 04: Rotate Me

## Description

| Program name | `rotate.py` |
| ------------ | ----------- |
| File to turn in | `load_image.py` `rotate.py` |
| Allowed functions | all libs for loading, manipulating, displaying image and table manipulation |

## Instructions

Create a program which must load the image "animal.jpeg", cut a square part of the image and transpose it to produce a counter-clockwise rotation of 90 degrees.
The program should display the rotated image, print the new shape and the data of the image the transposition.

No library is allowed for the transposition.

Expected output:

```bash
$> python rotate.py
The shape of image is: (400, 400, 1) or (400, 400)
[[[167]
[180]
[194]
...
[102]
[104]
[103]]]
New shape after Transpose: (400, 400)
[[167 180 194 ... 64 50 72]
...
[115 116 119 ... 102 104 103]]
$>
```

## References
- [Matrix Transpose using Nested Loop](https://www.programiz.com/python-programming/examples/transpose-matrix)
- [How do I create an empty array and then append to it in NumPy?](https://stackoverflow.com/questions/568962/how-do-i-create-an-empty-array-and-then-append-to-it-in-numpy)