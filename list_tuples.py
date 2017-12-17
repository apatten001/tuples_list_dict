
# a tuple is immutable and a list is mutable and use ()

var1 = "Sam"

# tuples can consist of floats ints variables strings and more
tup1 = ("Arnold", "Monte", "Jen", 12, var1)

print(tup1)


# this prints the length of objects in the tuple
print(len(tup1))

# list use []

list_1 = [1,3,4,6,8]

list_2  = ["Arnold", "Monte", "Jen", 12, var1]

print(list_1 + list_2)

# you can subset of what you want out of the list. Index starts at 0 and does not include last index num

print(list_2[4:])
print(list_2[:4])
print(list_2[1:3])

# negative number starts from the end

print(list_2[:-4])

print("\n" * 2)


# i can also change value in the list

list_2[0] = "AJ"

print(list_2)


# now I am going to store list inside of list

all_list = [list_1 , list_2]

print(all_list)

# if i want to get an item out of list_2 i would

print(all_list[1][2])

# this will add to a list you cannot append to tuple

list_2.append("I am added")
print(list_2)
# i can also remove an item

list_1.remove(3)
print(list_1)


del list_1[2]
print(list_1)


