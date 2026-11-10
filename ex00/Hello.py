ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# list
ft_list.append("World!")
# tuple
ft_tuple = ft_tuple[:1] + ("Germany!",)
# set
ft_set.remove("tutu!")
ft_set.add("Berlin!")
# dict
ft_dict["Hello"] = "42Berlin!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
