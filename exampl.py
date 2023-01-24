# import timeit

# code_to_test = """
# a = range(100000)
# b = [i*2 for i in a]
# """
#
# elapsed_time = timeit.timeit(code_to_test, number=100)/100
# print(elapsed_time)
#
# text = "text"
# for c in text:
#     if c == "t":
#         print(text.index(c))


# my_dict = {"Lermontov": "Yuriy", "Pushkin": "Aleksandr"}
# print(my_dict)
# print(my_dict["Lermontov"])
# my_dict["Lermontov"], my_dict["Pushkin"] = my_dict["Pushkin"], my_dict["Lermontov"]
# print(my_dict)


a = {"a": 1, "b": 2}
b = {"b": 3, "a": 4}

# print({**a, **b})
print({**a, **b})
