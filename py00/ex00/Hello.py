ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# modify list
world = "World!"
ft_list[-1] = world

# modify tuple
new_tuple = list(ft_tuple)
new_tuple.remove("toto!")
ft_tuple = tuple(new_tuple)
country = ("France!",)
ft_tuple += country

# modify set
city = "Paris!"
ft_set.remove("tutu!")
ft_set.add(city)

# modify dict
campus = "42Paris!"
ft_dict["Hello"] = campus

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)