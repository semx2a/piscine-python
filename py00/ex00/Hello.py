ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

""" ft_list = []
ft_tuple = ()
ft_set = {}
ft_dict = {}
 """
# modify list
world = "World!"
try:
	ft_list[-1] = world
except:
	print("Error: Issue with list!")

# modify tuple
try:
	new_tuple = list(ft_tuple)
	new_tuple.remove("toto!")
	ft_tuple = tuple(new_tuple)
	country = ("France!",)
	ft_tuple += country
except:
	print("Error: Issue with tupple")

# modify set
try:
	city = "Paris!"
	ft_set.remove("tutu!")
	ft_set.add(city)
except:
	print("Error: Issue with set!")

# modify dict
try:
	campus = "42Paris!"
	ft_dict["Hello"] = campus
except:
	print("Error: Issue with dict!")

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)