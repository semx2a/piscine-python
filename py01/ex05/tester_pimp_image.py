from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

landscape_img = ft_load("../assets/landscape.jpg")
cat_img = ft_load("../assets/cat.jpg")
animal_img = ft_load("../assets/animal.jpeg")
img = ft_load("../assets/image.png")

images = [landscape_img, cat_img, animal_img, img]

# print("Select the filter you would like to apply to the picutre:")

try:
    for image in images:
        ft_invert(image)
        ft_red(image)
        ft_green(image)
        ft_blue(image)
        ft_grey(image)

except Exception as e:
    print(f'Exception: {e}')

print("Functions docStrings:")
print(ft_invert.__doc__)
print(ft_red.__doc__)
print(ft_green.__doc__)
print(ft_blue.__doc__)
print(ft_grey.__doc__)
