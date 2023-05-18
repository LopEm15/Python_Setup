# create a function that greets you.

def hello():
    print ("Howdy y'all!")

# create a function named pack() that accepts 3 arguements, and returns a single list with the three are inside as list elements

def pack(a,b,c):
    return [a,b,c]

#create a function named eat_lunch(). This should accept a list of any length, and print out a series of strings that say "First I eat _"(the first element of the list), and "Next I eat _"(for the following elements in the list). If the list is empty, print "My lunchbox is empty!". this function should not return anything.

def eat_lunch(my_lst):
    if len(my_lst) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(my_lst)):
            if i == 0:
                print(f"First I eat {my_lst[0]}")
            else:
                print(f"Next I eat {my_lst[i]}")

# Now I need to call the functions in order for them to run

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["burrito"])
eat_lunch(["orange","chips","burrito","cookie"])