#  File: Intervals.py

#  Description: Read a set of intervals from a file. Collapse all the overlapping intervals and print the smallest set
#  of non-intersecting intervals in ascending order of the lower end of the interval.

#  Student Name: Kevin Jia

#  Date Created: 2/2

#  Date Last Modified: 2/4

def main():
    file = open("intervals.txt", "r")

    list_tuples = []

    # Add the tuples to a list
    for line in file:

        list1 = line.split(" ")
        list1[-1] = list1[-1].strip("\n")
        new_tuple = (int(list1[0]), int(list1[1]))

        list_tuples.append(new_tuple)

    # Sort the list
    list_tuples.sort()

    # Collapse all the overlapping intervals and add the smallest set of non-intersecting in ascending order of
    # the lower end of the interval to the result list

    result = []
    new_Tuple = list_tuples[0]

    for i in range(1, len(list_tuples)):
        current_tuple = list_tuples[i]
        if (current_tuple[1] >= new_Tuple[1] and current_tuple[0] <= new_Tuple[1]):
            new_Tuple = (new_Tuple[0], current_tuple[1])
        elif(current_tuple[1] <= new_Tuple[1] and current_tuple[0] <= new_Tuple[1]):
            new_Tuple = (new_Tuple[0], new_Tuple[1])
        else:
            result.append(new_Tuple)
            new_Tuple = (current_tuple[0], current_tuple[1])

    # Add the last tuple to the result list
    result.append(new_Tuple)

    # Print the intervals
    print("Non-intersecting Intervals:")
    for item in result:
        print(item)

    # Bonus:

    # Create a dictionary to store the tuples as keys and their size as values
    dict = {}
    ordered_list = []

    # Find the size of the tuples
    for item in result:
        difference = abs(item[1] - item[0])
        dict[item] = difference
        ordered_list.append(difference)

    print("Non-intersecting Intervals in order of size:")

    # Sort the tuples in ascending order
    ordered_list.sort()

    # Print the intervals in order of size
    for item in ordered_list:
        for key, value in dict.items():
            if value == item:
                print(key)


main()
