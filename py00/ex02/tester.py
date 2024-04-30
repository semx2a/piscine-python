import find_ft_type as fft

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

fft.all_thing_is_obj(ft_list)
fft.all_thing_is_obj(ft_tuple)
fft.all_thing_is_obj(ft_set)
fft.all_thing_is_obj(ft_dict)
fft.all_thing_is_obj("Brian")
fft.all_thing_is_obj("Toto")

print(fft.all_thing_is_obj(10))