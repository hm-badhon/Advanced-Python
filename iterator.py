

# # Simple iterator

# # List

# for i in [1,2,3,4]:
#     print(i)

# print("\n")

# # Strings

# for char in "badhon":
#     print(char)

# print("\n")

# # Dictionary

# for k in {"a":1,"b":2}:
#     print(k)


# # define a list 

my_list = [34,56,2,15]
print(my_list)
# get an iterator using iter()
my_iter = iter(my_list)

print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# No more data raise the StopIteration()
print(next(my_iter))
continue
#Create an iterator object from that iterable
new_list = [21,346,7,9534,45,4]
iter_obj = iter(new_list)

# infinte loop

while True:
    try:
        #get the next item
        element = next(iter_obj)
        print(element)
    except StopIteration:
        print(" Stop Iteration ")
        # if stopiteration is raised, break from loop
        break












