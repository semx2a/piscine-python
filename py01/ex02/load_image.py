import PIL as Image
#import matplotlib.pyplot as plt
import numpy as np


def ft_load(path: str) -> array:

    image = Image.open(path)
    print(image.format)
    print(image.size)
    print(image.mode)
    
    return np.array()